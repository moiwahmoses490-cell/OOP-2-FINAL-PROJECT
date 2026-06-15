import asyncio
from database import AsyncSessionLocal
import models
import crud

async def main():
    async with AsyncSessionLocal() as db:
        # Get all employers
        import sqlalchemy
        res = await db.execute(sqlalchemy.future.select(models.User).where(models.User.role == "employer"))
        employers = res.scalars().all()
        for emp in employers:
            print(f"\nEmployer: {emp.username} (ID: {emp.id})")
            apps = await crud.get_applications_for_employer_jobs(db, employer_id=emp.id)
            print(f"Number of applications returned: {len(apps)}")
            for a in apps:
                print(f"  - App ID: {a.id}, Job ID: {a.job_id}, Job Title: {a.job.title if a.job else 'None'}")

if __name__ == "__main__":
    asyncio.run(main())
