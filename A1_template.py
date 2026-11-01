#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CS441 Algorithm Analysis and Design — Assignment A1 (Greedy)
อัลกอริทึมเชิงละโมบ: รถกระบะขนผลไม้ไปตลาดไท (Fractional Knapsack)
=====================================================================

วิธีใช้
    1. แก้ไขค่าใน BLOCK 1 ให้เป็นข้อมูลของตนเอง (รหัสนักศึกษา 10 หลักต้องถูกต้อง)
    2. เติมโค้ดในฟังก์ชันที่มีเครื่องหมาย TODO ใน BLOCK 3, 4, 5 และเติมคำตอบใน BLOCK 6
    3. รันทดสอบ:  python3 A1_template.py
    4. บันทึกไฟล์เป็น  A1_Greedy_<รหัสนักศึกษา>.py  เช่น  A1_Greedy_1350701288.py  แล้วส่งใน MS Teams

กติกา
    - ใช้ Python 3.10 ขึ้นไป ใช้ได้เฉพาะ standard library (fractions, math, sys)
    - ห้ามใช้ library ภายนอก เช่น numpy, pulp, networkx
    - ห้ามแก้ไข BLOCK 2 และ BLOCK 7 (โปรแกรมตรวจจะคำนวณข้อมูลเองจากรหัสนักศึกษา)
    - ค่าตัวเลขทุกค่าให้ใช้ fractions.Fraction เพื่อความแม่นยำ (ห้ามปัดเศษ)
    - ใช้ sorted() หรือ list.sort() ได้ (งานนี้ประเมินอัลกอริทึมเชิงละโมบ ไม่ใช่การเรียงลำดับ)
"""
from fractions import Fraction
import sys

# =====================================================================
# BLOCK 1 — ข้อมูลนักศึกษา  (แก้ไขเฉพาะค่าในบล็อกนี้)
# =====================================================================
STUDENT_ID   = "0000000000"          # รหัสนักศึกษา 10 หลัก  เช่น "1350701288"
STUDENT_NAME = "ชื่อ นามสกุล"          # ชื่อ-นามสกุล ภาษาไทย
COURSE       = "CS441 Algorithm Analysis and Design"
SECTION      = "327X"                # กลุ่มเรียน เช่น 327A / 327B / 327C
ASSIGNMENT   = "Assignment A1 - Greedy: Fractional Knapsack"


# =====================================================================
# BLOCK 2 — ข้อมูลโจทย์ส่วนตัว  (ห้ามแก้ไข)
#   คำนวณ d1..d5 จาก 5 หลักท้ายของรหัสนักศึกษา (หลักที่เป็น 0 ใช้ 10)
#   แล้วสร้างตารางผลไม้ 5 ชนิดและความจุรถ W
# =====================================================================
FRUIT_NAMES = {"A": "ทุเรียน", "B": "มังคุด", "C": "เงาะ", "D": "ลองกอง", "E": "มะม่วง"}


def get_d_values(student_id):
    """คืน [d1, d2, d3, d4, d5] จาก 5 หลักท้ายของรหัสนักศึกษา (0 -> 10)"""
    last5 = str(student_id).strip()[-5:].zfill(5)
    return [10 if c == "0" else int(c) for c in last5]


def build_items(d):
    """สร้างรายการผลไม้ 5 ชนิด  แต่ละชนิดเป็น dict:
        {"code": "A", "name": "ทุเรียน", "weight": Fraction, "profit": Fraction}
    weight = น้ำหนักทั้งล็อต (กก.)   profit = กำไรถ้ารับซื้อทั้งล็อต (บาท)
    """
    d1, d2, d3, d4, d5 = d
    spec = [("A", 10 * d2, 100 * d3),
            ("B", 10 * d3,  60 * d4),
            ("C", 10 * d4,  40 * d5),
            ("D", 10 * d5,  80 * d1),
            ("E", 10 * d1,  50 * d2)]
    return [{"code": c, "name": FRUIT_NAMES[c], "weight": Fraction(w), "profit": Fraction(v)}
            for c, w, v in spec]


def capacity(d):
    """ความจุรถกระบะ W = 5 * (d1 + d2 + d3 + d4 + d5) กก.  (ครึ่งหนึ่งของผลผลิตทั้งหมด)"""
    return Fraction(5 * sum(d))


# =====================================================================
# BLOCK 3 — ข้อ (ก) จัดเตรียมข้อมูล  [6 คะแนน]
# =====================================================================
def profit_rate(item):
    """(ก.2) คืนอัตรากำไรต่อกิโลกรัม r = profit / weight ของผลไม้ 1 ชนิด (Fraction)"""
    # TODO: implement
    pass


def sort_by_rate(items):
    """(ก.3) คืน list ใหม่ที่เรียงผลไม้ตาม profit_rate จากมากไปน้อย
    ถ้าอัตราเท่ากัน ให้ชนิดที่รหัสตัวอักษรมาก่อนอยู่ก่อน (A ก่อน B ก่อน C ...)
    ห้ามแก้ไข list เดิม
    """
    # TODO: implement
    pass


# =====================================================================
# BLOCK 4 — ข้อ (ข) Fractional Knapsack  [10.5 คะแนน]
# =====================================================================
def fractional_knapsack(items, W):
    """รันอัลกอริทึมเชิงละโมบตามหัวข้อ 5.6: รับซื้อผลไม้ตามลำดับอัตรากำไรต่อกิโลกรัม
    ทั้งล็อตจนกว่าจะพบล็อตที่ใส่ไม่พอ จึงรับซื้อบางส่วนให้รถเต็มพอดีแล้วหยุด

    คืน dict:
        "plan":  list ของ dict ตามลำดับที่รับซื้อ (เฉพาะชนิดที่รับซื้อ > 0)
                 {"code": "B", "take": Fraction(กก.ที่รับซื้อ), "profit": Fraction(กำไรที่ได้),
                  "remain": Fraction(น้ำหนักคงเหลือของรถหลังรับซื้อ)}
        "x":     dict code -> Fraction สัดส่วนที่รับซื้อ (0 ถึง 1) ครบทั้ง 5 ชนิด
        "total": Fraction กำไรรวม
        "split": code ของชนิดที่ถูกรับซื้อเพียงบางส่วน หรือ None ถ้าไม่มี
    """
    # TODO: implement
    pass


# =====================================================================
# BLOCK 5 — ข้อ (ค) ล็อตที่แบ่งไม่ได้  [7.5 คะแนน]
# =====================================================================
def knapsack_one_indivisible(items, W, k):
    """ผลไม้ชนิด k ต้องรับซื้อทั้งล็อตหรือไม่รับซื้อเลย ส่วนอีก 4 ชนิดแบ่งได้ตามเดิม
    ให้พิจารณา 2 กรณีแล้วเลือกกรณีที่กำไรสูงกว่า

        กรณี "out": ไม่รับซื้อ k  -> รัน fractional_knapsack กับ 4 ชนิดที่เหลือ ความจุ W
        กรณี "in" : รับซื้อ k ทั้งล็อต -> ได้กำไร profit_k, ความจุเหลือ W - weight_k
                    แล้วรัน fractional_knapsack กับ 4 ชนิดที่เหลือ ความจุที่เหลือ
                    (ถ้า weight_k > W กรณีนี้ทำไม่ได้ ให้กำไร = -1)

    คืน dict:
        "case_out": Fraction กำไรรวมกรณี out
        "case_in":  Fraction กำไรรวมกรณี in  (หรือ Fraction(-1) ถ้าทำไม่ได้)
        "best":     "out" หรือ "in"  (ถ้าเท่ากันให้ตอบ "out")
        "best_total": Fraction กำไรของกรณีที่เลือก
    """
    # TODO: implement
    pass


# =====================================================================
# BLOCK 6 — ข้อ (ง) สัญกรณ์เชิงเส้นกำกับ (บทที่ 3)  [6 คะแนน]
#   ให้ n = จำนวนชนิดผลไม้  เติมสัญกรณ์ Big-O ที่แน่นที่สุดของโค้ดที่ตนเองเขียน
#   รูปแบบคำตอบ เช่น "O(1)", "O(n)", "O(n log n)", "O(n^2)"
# =====================================================================
BIG_O = {
    "profit_rate_all":          "O(?)",   # คำนวณอัตรากำไรของผลไม้ทุกชนิด
    "sort_by_rate":             "O(?)",   # การเรียงลำดับตามอัตรากำไร
    "take_loop":                "O(?)",   # วงวนรับซื้อทีละชนิดใน fractional_knapsack
    "fractional_knapsack":      "O(?)",   # ทั้งฟังก์ชัน (ข)
    "knapsack_one_indivisible": "O(?)",   # ทั้งฟังก์ชัน (ค)
}

BIG_O_REASON = """
(เขียนคำอธิบายสั้น ๆ 3-5 บรรทัด ว่าขั้นตอนใดเป็นตัวกำหนด (dominate) เวลาทำงานของ (ข) และ (ค)
 และเหตุใด (ค) จึงไม่ได้ช้ากว่า (ข) ในเชิงเส้นกำกับ)
"""


# =====================================================================
# BLOCK 7 — main: รันทุกข้อและพิมพ์ผลในรูปแบบมาตรฐาน  (ห้ามแก้ไข)
# =====================================================================
def _fmt(v):
    """แปลงตัวเลขเป็นข้อความ: จำนวนเต็ม -> '12', เศษส่วน -> '7/16'"""
    if v is None:
        return "None"
    if isinstance(v, bool):
        return str(v)
    try:
        f = v if isinstance(v, Fraction) else Fraction(str(v))
    except Exception:
        return str(v)
    f = f.limit_denominator(10 ** 9)
    return str(f.numerator) if f.denominator == 1 else f"{f.numerator}/{f.denominator}"


def _safe(label, fn, *args):
    """เรียกฟังก์ชันของนักศึกษาแบบปลอดภัย: ถ้า error หรือยังเป็น TODO ให้พิมพ์แจ้งแล้วไปต่อ"""
    try:
        r = fn(*args)
    except Exception as e:  # noqa: BLE001
        print(f"[{label}] ERROR {type(e).__name__}: {e}")
        return None
    if r is None:
        print(f"[{label}] TODO")
    return r


def main():
    d = get_d_values(STUDENT_ID)
    items = build_items(d)
    W = capacity(d)

    print(f"[INFO] id={STUDENT_ID} name={STUDENT_NAME} course={COURSE} section={SECTION} assignment={ASSIGNMENT}")
    print(f"[D] d1={d[0]} d2={d[1]} d3={d[2]} d4={d[3]} d5={d[4]}")
    print(f"[W] {_fmt(W)}")
    for it in items:
        print(f"[A1] {it['code']} {it['name']} w={_fmt(it['weight'])} v={_fmt(it['profit'])}")

    # ---- (ก) ----
    rates_ok = True
    for it in items:
        r = _safe("A2", profit_rate, it)
        if r is None:
            rates_ok = False
            break
        print(f"[A2] {it['code']} r={_fmt(r)}")
    order = _safe("A3", sort_by_rate, items) if rates_ok else None
    if order:
        print("[A3] order=" + ",".join(it["code"] for it in order))

    # ---- (ข) ----
    res = _safe("B1", fractional_knapsack, items, W)
    split = None
    if res:
        for i, p in enumerate(res["plan"], 1):
            print(f"[B1] step={i} code={p['code']} take={_fmt(p['take'])} profit={_fmt(p['profit'])} remain={_fmt(p['remain'])}")
        print("[B2] x " + " ".join(f"{c}={_fmt(res['x'].get(c))}" for c in "ABCDE"))
        split = res.get("split")
        print(f"[B2] split={split}")
        weight_used = sum(res["x"].get(it["code"], 0) * it["weight"] for it in items)
        print(f"[B3] total={_fmt(res['total'])} weight={_fmt(weight_used)}")

    # ---- (ค) ----
    k = split
    if res and k is None and order:
        for it in order:                      # ไม่มีชนิดที่ถูกแบ่ง -> ใช้ชนิดถัดไปที่ยังไม่ได้รับซื้อ
            if res["x"].get(it["code"], 0) == 0:
                k = it["code"]
                break
    if k is None:
        k = "C"                               # ค่าสำรองเมื่อ (ข) ยังไม่เสร็จ เพื่อให้ (ค) ทดสอบได้
    print(f"[C0] k={k}")
    resc = _safe("C1", knapsack_one_indivisible, items, W, k)
    if resc:
        print(f"[C1] case_out={_fmt(resc['case_out'])}")
        print(f"[C2] case_in={_fmt(resc['case_in'])}")
        print(f"[C3] best={resc['best']} best_total={_fmt(resc['best_total'])}")

    # ---- (ง) ----
    for key, val in BIG_O.items():
        print(f"[D] {key}={val}")
    print("[D_REASON] " + " ".join(BIG_O_REASON.split()))


if __name__ == "__main__":
    if STUDENT_ID == "0000000000" or not STUDENT_ID.isdigit() or len(STUDENT_ID) != 10:
        print("กรุณาแก้ไข STUDENT_ID ใน BLOCK 1 ให้เป็นรหัสนักศึกษา 10 หลักของตนเอง")
        sys.exit(1)
    main()
