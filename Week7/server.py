"""Race-condition-safe coupon server for Week 7.

Run with: uvicorn server:app --reload --port 8088
"""

import asyncio
from typing import Dict, List

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Week 7 Coupon Server")
STUDENTS = [f"Student_{number:02d}" for number in range(1, 6)]
coupons_db = [f"COUPON-{number:02d}" for number in range(1, len(STUDENTS) * 2)]
current_coupon_index = 0
student_claims: Dict[str, List[str]] = {student: [] for student in STUDENTS}
coupon_lock = asyncio.Lock()


class ClaimRequest(BaseModel):
	student_id: str


@app.get("/")
async def root() -> dict[str, str]:
	return {"service": "week7-secure-coupon-server", "status": "ok"}


@app.post("/claim")
async def claim_coupon(request: ClaimRequest) -> dict[str, str | int]:
	global current_coupon_index
	student_id = request.student_id
	if student_id not in student_claims:
		return {"status": "INVALID_STUDENT", "message": "Unknown student"}
	async with coupon_lock:
		if len(student_claims[student_id]) >= 2:
			return {"status": "LIMIT_REACHED", "message": "You already have two coupons"}
		if current_coupon_index >= len(coupons_db):
			return {"status": "OUT_OF_STOCK", "message": "No coupons remain"}
		await asyncio.sleep(0.1)
		coupon = coupons_db[current_coupon_index]
		current_coupon_index += 1
		student_claims[student_id].append(coupon)
		return {"status": "SUCCESS", "claimed_coupon": coupon, "total_owned": len(student_claims[student_id])}


@app.get("/summary")
async def summary() -> dict[str, object]:
	async with coupon_lock:
		return {"remaining_stock": len(coupons_db) - current_coupon_index, "student_claims": student_claims}
