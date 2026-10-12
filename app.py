# ============================================================
# QUẢN LÝ ĐIỂM SINH VIÊN - Web App bằng Streamlit
# ============================================================
import streamlit as st
import pandas as pd

# --- Thông tin người thực hiện ---
TEN_SV = "Tông Đăng Dương"
MSSV = "ĐIỀN MSSV CỦA BẠN"

# 1. Tạo frame dữ liệu
ho_ten     = ["Nguyễn Văn An", "Trần Thị Bình", "Lê Hoàng Cường", "Phạm Minh Dũng", "Võ Thị Em",              "Đặng Quốc Phong", "Hoàng Thị Giang", "Bùi Thanh Hải", "Ngô Thị Hương", "Lý Văn Khang"]
chuyen_can = [9, 10, 8, 7, 9, 6, 10, 8, 9, 7]
giua_ky    = [8, 9, 6.5, 5, 7.5, 4, 8.5, 7, 9, 6.5]
cuoi_ky    = [8.5, 9.5, 7, 4.5, 8, 3.5, 9, 6.5, 8, 7.5]

bang_diem = pd.DataFrame({
    "Họ tên": ho_ten,
    "Chuyên cần": chuyen_can,
    "Giữa kỳ": giua_ky,
    "Cuối kỳ": cuoi_ky
})

# 2. Tính điểm tổng kết và xếp loại
bang_diem["Tổng kết"] = bang_diem["Chuyên cần"] * 0.1 + bang_diem["Giữa kỳ"] * 0.3 + bang_diem["Cuối kỳ"] * 0.6
bang_diem["Tổng kết"] = bang_diem["Tổng kết"].round(2)

xep_loai = []
for diem in bang_diem["Tổng kết"]:
    if diem >= 9:
        xep_loai.append("Xuất sắc")
    elif diem >= 8:
        xep_loai.append("Giỏi")
    elif diem >= 7:
        xep_loai.append("Khá")
    elif diem >= 5:
        xep_loai.append("Trung bình")
    else:
        xep_loai.append("Yếu")
bang_diem["Xếp loại"] = xep_loai

# 3. Thống kê
diem_tb = round(bang_diem["Tổng kết"].mean(), 2)
vi_tri_cao = bang_diem["Tổng kết"].idxmax()
ten_cao = bang_diem.loc[vi_tri_cao, "Họ tên"]
diem_cao = bang_diem.loc[vi_tri_cao, "Tổng kết"]

vi_tri_thap = bang_diem["Tổng kết"].idxmin()
ten_thap = bang_diem.loc[vi_tri_thap, "Họ tên"]
diem_thap = bang_diem.loc[vi_tri_thap, "Tổng kết"]

so_dat = 0
for diem in bang_diem["Tổng kết"]:
    if diem >= 5:
        so_dat = so_dat + 1

# 4. Hiển thị lên web bằng Streamlit
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

st.header("1. Bảng điểm của 10 sinh viên")
st.dataframe(bang_diem)

st.header("2. Thống kê")
st.write("Điểm trung bình của lớp:", diem_tb)
st.write("Sinh viên có điểm tổng kết cao nhất:", ten_cao, "-", diem_cao, "điểm")
st.write("Sinh viên có điểm tổng kết thấp nhất:", ten_thap, "-", diem_thap, "điểm")
st.write("Số sinh viên đạt:", so_dat, "/", len(bang_diem))

st.header("3. Xem điểm từng sinh viên")
ten_chon = st.selectbox("Chọn một sinh viên:", bang_diem["Họ tên"])
sv = bang_diem[bang_diem["Họ tên"] == ten_chon].iloc[0]
st.write("Chuyên cần:", sv["Chuyên cần"])
st.write("Giữa kỳ:", sv["Giữa kỳ"])
st.write("Cuối kỳ:", sv["Cuối kỳ"])
st.write("Điểm tổng kết:", sv["Tổng kết"])
st.write("Xếp loại:", sv["Xếp loại"])

st.header("4. Biểu đồ điểm tổng kết")
st.bar_chart(bang_diem.set_index("Họ tên")["Tổng kết"])

st.divider()
st.markdown(
    "<p style='font-size:12px; font-weight:bold;'>Người thực hiện: " + TEN_SV + " - MSSV: " + MSSV + "</p>",
    unsafe_allow_html=True
)
