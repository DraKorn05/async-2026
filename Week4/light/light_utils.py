# light_utils.py
import httpx

BASE_URL = "http://172.16.2.117:8088"


async def control_light(student_id: str, light_id: str, status: str) -> dict:
    """
    ยิง POST ไปเปิด/ปิดไฟดวงหนึ่งของ student_id ที่ระบุ
    Response จะรอจนกว่า simulated hardware delay ของไฟดวงนั้นจะครบก่อนถึงจะตอบกลับ
    (เช่น light_3 ดีเลย์ 2.0s -> ฟังก์ชันนี้จะ await ค้างอยู่ 2.0s ก่อนได้ผลลัพธ์)
    """
    url = f"{BASE_URL}/api/{student_id}/lights/{light_id}"
    payload = {"status": status.upper()}
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(url, json=payload, timeout=10.0)
            if response.status_code == 200:
                return response.json()
            return {"status": "ERROR", "detail": f"HTTP Error {response.status_code}"}
    except Exception as e:
        return {"status": "ERROR", "detail": f"Connection failed: {e}"}


async def reset_lights(student_id: str) -> dict:
    """รีเซ็ตไฟทุกดวงของ student_id กลับเป็น OFF"""
    url = f"{BASE_URL}/api/{student_id}/lights/reset"
    try:
        async with httpx.AsyncClient() as client:
            response = await client.delete(url, timeout=10.0)
            return response.json()
    except Exception as e:
        return {"status": "ERROR", "detail": f"Connection failed: {e}"}