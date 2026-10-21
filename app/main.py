from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(
    title="EcoGrid Qatar (Q-Carbon API)",
    description="Microservice for calculating carbon and desalinated water footprints in Qatar & GCC",
    version="1.0.0"
)

# Regional Emission Factors
GRID_EMISSION_FACTOR = 0.512         # kg CO2e per kWh (Qatar Grid profile)
PETROL_EMISSION_FACTOR = 2.31        # kg CO2e per Liter of Gasoline
DESAL_WATER_EMISSION_FACTOR = 4.2    # kg CO2e per m3 desalinated water

class CarbonRequest(BaseModel):
    electricity_kwh: float = Field(..., ge=0, description="Monthly electricity usage in kWh")
    ac_percentage: float = Field(65.0, ge=0, le=100, description="Estimated % of power used by AC")
    petrol_liters: float = Field(0.0, ge=0, description="Monthly fuel consumed in Liters")

class WaterRequest(BaseModel):
    water_m3: float = Field(..., ge=0, description="Monthly water usage in cubic meters (m3)")

@app.get("/")
def read_root():
    return {
        "status": "online",
        "service": "EcoGrid Qatar (Q-Carbon API)",
        "region": "Qatar / GCC",
        "docs": "/docs"
    }

@app.post("/api/v1/calculate/carbon")
def calculate_carbon(data: CarbonRequest):
    electricity_co2 = data.electricity_kwh * GRID_EMISSION_FACTOR
    ac_co2 = electricity_co2 * (data.ac_percentage / 100.0)
    fuel_co2 = data.petrol_liters * PETROL_EMISSION_FACTOR
    total_co2 = electricity_co2 + fuel_co2

    return {
        "total_co2_kg": round(total_co2, 2),
        "breakdown": {
            "electricity_co2_kg": round(electricity_co2, 2),
            "estimated_ac_share_kg": round(ac_co2, 2),
            "fuel_co2_kg": round(fuel_co2, 2)
        },
        "unit": "kg CO2e / month"
    }

@app.post("/api/v1/calculate/water")
def calculate_water(data: WaterRequest):
    water_co2 = data.water_m3 * DESAL_WATER_EMISSION_FACTOR
    
    return {
        "water_consumed_m3": data.water_m3,
        "desalination_co2_kg": round(water_co2, 2),
        "note": "Based on seawater processing and grid power profiles in Qatar.",
        "unit": "kg CO2e / month"
    }
