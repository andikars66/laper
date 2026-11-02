"""Dissolve existing SubSLS boundaries into lazy-loaded village/district outlines."""
import json
from pathlib import Path

from shapely import make_valid, union_all
from shapely.geometry import mapping, shape


def polygon_parts(geometry):
    if geometry.geom_type == "Polygon":
        return [geometry]
    if hasattr(geometry, "geoms"):
        return [part for child in geometry.geoms for part in polygon_parts(child)]
    return []


def outline(features):
    # Repair invalid rings; collapsed lines/points are not an area boundary.
    polygons = [part for f in features for part in polygon_parts(make_valid(shape(f["geometry"])))]
    geometry = union_all(polygons)
    if geometry.geom_type not in ("Polygon", "MultiPolygon"):
        raise ValueError(f"Unexpected dissolved geometry: {geometry.geom_type}")
    return {"geometry": mapping(geometry), "bbox": list(geometry.bounds)}


def prepare_stamp_boundaries(data_dir):
    output_dir = data_dir / "regions"
    output_dir.mkdir(exist_ok=True)
    for source in sorted((data_dir / "boundaries").glob("*.json")):
        collection = json.loads(source.read_text(encoding="utf-8"))
        villages = {}
        for feature in collection["features"]:
            villages.setdefault(feature["properties"]["iddesa"], []).append(feature)
        result = {
            "kecamatan": outline(collection["features"]),
            "desa": {code: outline(features) for code, features in villages.items()},
        }
        target = output_dir / source.name
        target.write_text(json.dumps(result, separators=(",", ":")), encoding="utf-8")
        print(f"Saved {target.name}: {len(villages)} village outlines ({target.stat().st_size / 1024:.1f} KB)")


if __name__ == "__main__":
    prepare_stamp_boundaries(Path(__file__).resolve().parents[1] / "public" / "data")
