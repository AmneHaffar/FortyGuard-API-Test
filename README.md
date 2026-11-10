# FortyGuard Temperature API – Heatmap Analysis

## Project Overview

This project demonstrates the integration of the **FortyGuard Temperature API** using Python to generate, retrieve, and analyze urban temperature heatmap data.

The objective is to explore FortyGuard's temperature intelligence capabilities and understand how geospatial temperature data can support urban climate analysis.

## Technologies Used

- Python 3
- Requests library
- FortyGuard Temperature API
- GeoJSON
- JSON
- Git & GitHub
- Visual Studio Code

## Project Structure

| File | Description |
|---|---|
| `test_api.py` | Submits a heatmap generation request to the FortyGuard API. |
| `check_status.py` | Checks the task status and saves the completed heatmap results. |
| `show_stats.py` | Extracts and displays temperature statistics from the generated heatmap. |
| `.gitignore` | Excludes local configuration and generated data files from Git tracking. |

## Workflow

**Step 1 – Submit Heatmap Request**

A POST request is sent to the FortyGuard API with a GeoJSON polygon, a specified date and time, and a spatial resolution.

The API returns a unique `activity_id` to track the submitted task.

**Step 2 – Check Task Status**

The returned activity ID is used to check the processing status through the API.

The task was successfully completed, returning HTTP status `200` and task status `Completed`.

**Step 3 – Retrieve and Analyze Results**

The completed response contains:

- `map_data`: GeoJSON features containing spatial temperature information.
- `stats_data`: Aggregated temperature statistics.

The results are saved locally in `heatmap_result.json` and analyzed using Python.

## Experimental Results

The successful heatmap request generated **150 temperature tiles** for a sample area in New York City.

| Metric | Result |
|---|---|
| Number of tiles | 150 |
| Minimum temperature | 31.887 °C |
| Maximum temperature | 33.1424 °C |
| Mean temperature | 32.2552 °C |
| Standard deviation | 0.4149 °C |
| Spatial resolution | 100 m |

These results demonstrate how the API provides spatially distributed temperature information and summary statistics for an urban area.

## Challenges and Lessons Learned

During the implementation, the initial API requests returned an HTTP `400` error related to geographic coverage.

After reviewing the API documentation and adjusting the request format, the heatmap submission completed successfully.

This experience helped demonstrate the importance of validating API request parameters, interpreting error responses, and tracking asynchronous tasks.

## Security

The FortyGuard API key is accessed through the `FORTYGUARD_API_KEY` environment variable rather than being hardcoded into the Python scripts.

Sensitive configuration files and generated output data are excluded from version control.

## Conclusion

This project successfully demonstrates an end-to-end workflow for integrating the FortyGuard Temperature API with Python, including heatmap submission, asynchronous status tracking, result retrieval, and temperature statistics analysis.

The project provides a foundation for further exploration of geospatial temperature visualization, urban heat analysis, and climate-aware applications.

## References

- [FortyGuard Official Website](https://fortyguard.com)
- [FortyGuard API Documentation](https://docs-api.fortyguard.com)