# Logistics Data Analysis — Week 1

## Project overview
This project supports a Week 1 logistics data analyst task. It outlines a data-driven approach to studying delivery delays, delivery duration, and operational efficiency for a fictional e-commerce logistics company.

## Objectives
- Explore delivery records and check data quality.
- Calculate example logistics KPIs where the required columns are available.
- Demonstrate a baseline regression model to estimate delivery duration.
- Use the results to inform future delivery planning and resource allocation.

## KPIs
1. **On-time delivery rate:** percentage of completed deliveries made by the promised time.
2. **Average delivery duration:** mean time between dispatch and delivery.
3. **Average delay:** average lateness relative to the promised delivery time, if available.
4. **Cost per delivery:** total operating cost divided by completed deliveries, if cost data is available.
5. **Prediction error (MAE):** average absolute difference between predicted and actual duration.

## Files
- `logistics_analysis.py` — example Python workflow for inspecting data, calculating basic KPIs, and fitting a baseline regression model.

## Requirements
Python 3.9 or newer is recommended. Install the packages with:

```bash
pip install pandas numpy scikit-learn
```

## How to run
1. Put a CSV file named `deliveries.csv` in the same folder as `logistics_analysis.py`.
2. Check the column names in your CSV.
3. Update the script if necessary. The example expects `dispatch_time` and `delivery_time` to calculate duration. Optional columns include `distance_km` and `promised_delivery_time`.
4. Run:

```bash
python logistics_analysis.py
```

## Example data format
The script is a template and does not include real delivery data. A compatible CSV might contain:

| dispatch_time | delivery_time | distance_km | promised_delivery_time |
|---|---|---:|---|
| 2026-10-01 09:00:00 | 2026-10-01 09:45:00 | 12.5 | 2026-10-01 10:00:00 |

Use real or public data and check its licence and documentation before analysis.

## Important limitations
- The column names must match the dataset or be updated in the code.
- Results depend on the quality and representativeness of the data.
- A public transport-trip dataset is not necessarily a parcel-delivery dataset.
- This is an educational baseline, not a production delivery-routing system.
- Do not claim model accuracy or business savings until you have actually run and evaluated the analysis.

## Proposed future work
Explore delivery patterns by zone and time of day, compare models, and investigate route optimisation subject to vehicle capacity, delivery windows, driver hours, and safety constraints.
