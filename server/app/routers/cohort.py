from fastapi import APIRouter

router = APIRouter(prefix="/api/cohort", tags=["Cohort"])


@router.get("/stats/{cohort_name}")
async def get_cohort_stats(cohort_name):
    return {"msg": f"These are your stats for {cohort_name}"}


@router.get("/attendance/{cohort_name}")
async def get_cohort_attendance_stat(cohort_name):
    return {"msg": f"These are your attendance stats {cohort_name}"}
