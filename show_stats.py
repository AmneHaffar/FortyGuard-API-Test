
import json

with open("heatmap_result.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Get heatmap tiles
features = data.get("map_data", {}).get("features", [])

print("=== FortyGuard Heatmap Summary ===")
print("Number of tiles:", len(features))

# Show first five tiles
print("\nFirst 5 tiles:")

for tile in features[:5]:
    properties = tile.get("properties", {})
    print(
        "Tile:", properties.get("tile_id"),
        "| Temperature:",
        properties.get("average_temperature"),
        "C"
    )

# Show temperature statistics
print("\n=== Temperature Statistics ===")

stats = data.get("stats_data", {})

temperature_stats = (
    stats.get("Temperature_stats")
    or stats.get("temperature_stats")
)

if temperature_stats:
    print(json.dumps(temperature_stats, indent=2))
else:
    print("Available statistics fields:", list(stats.keys()))
    print(json.dumps(stats, indent=2)[:2000])
