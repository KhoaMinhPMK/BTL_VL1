"""
BÀI 8: VẼ QUỸ ĐẠO VÀ XÁC ĐỊNH VECTOR MÔMEN ĐỘNG LƯỢNG CỦA CHUYỂN ĐỘNG
VỚI PHƯƠNG TRÌNH CHO BỞI x(t) VÀ y(t)

Công thức: L = r × p = m(r × v)
Trong đó:
- L: vector mômen động lượng
- r: vector vị trí (x, y)
- p: động lượng
- m: khối lượng
- v: vector vận tốc (vx, vy)
"""

import numpy as np
import matplotlib.pyplot as plt
from sympy import *
from matplotlib import rcParams

# Cấu hình để hiển thị tiếng Việt
rcParams['font.family'] = 'sans-serif'
rcParams['axes.unicode_minus'] = False

def tinh_momen_dong_luong():
    """
    Hàm chính để tính toán và vẽ đồ thị quỹ đạo và mômen động lượng
    """
    
    print("="*70)
    print("BÀI 8: TÍNH TOÁN MOMEN DONG LUONG VA VE QUY DAO CHUYEN DONG")
    print("="*70)
    
    # Khai báo biến symbolic
    t = symbols('t')
    
    # Bước 1: Nhập biểu thức x(t) và y(t)
    print("\nNhap bieu thuc chuyen dong (su dung bien 't'):")
    print("Vi du: t**2, sin(t), cos(t), exp(t), sqrt(t), etc.")
    print("-"*70)
    
    x_input = input("Nhap bieu thuc x(t): ")
    y_input = input("Nhap bieu thuc y(t): ")
    
    try:
        x_t = sympify(x_input)
        y_t = sympify(y_input)
    except:
        print("Loi: Bieu thuc khong hop le!")
        return
    
    print(f"\nBieu thuc chuyen dong:")
    print(f"x(t) = {x_t}")
    print(f"y(t) = {y_t}")
    
    # Nhập khối lượng
    m_input = input("\nNhap khoi luong m (kg) [mac dinh = 1]: ")
    m = float(m_input) if m_input.strip() else 1.0
    
    # Nhập khoảng thời gian
    t_start = float(input("Nhap thoi gian bat dau t_start (s) [mac dinh = 0]: ") or "0")
    t_end = float(input("Nhap thoi gian ket thuc t_end (s) [mac dinh = 10]: ") or "10")
    n_points = int(input("Nhap so diem tinh toan [mac dinh = 1000]: ") or "1000")
    
    print("\n" + "="*70)
    print("TINH TOAN SYMBOLIC")
    print("="*70)
    
    # Bước 2: Tính vận tốc bằng đạo hàm
    vx_t = diff(x_t, t)
    vy_t = diff(y_t, t)
    
    print(f"\nVan toc:")
    print(f"vx(t) = dx/dt = {vx_t}")
    print(f"vy(t) = dy/dt = {vy_t}")
    
    # Bước 3: Tính mômen động lượng
    # L = r × p = m(r × v)
    # Trong 2D: L = m(x*vy - y*vx) (hướng vuông góc với mặt phẳng)
    L_z = m * (x_t * vy_t - y_t * vx_t)
    L_z_simplified = simplify(L_z)
    
    print(f"\nMomen dong luong (thanh phan z):")
    print(f"L_z = m(x*vy - y*vx) = {L_z_simplified}")
    
    # Tính độ lớn mômen động lượng
    L_magnitude = abs(L_z)
    
    print(f"\nDo lon momen dong luong:")
    print(f"|L| = {L_magnitude}")
    
    # Bước 4: Chuyển đổi sang hàm số để vẽ đồ thị
    print("\n" + "="*70)
    print("TINH TOAN SO VA VE DO THI")
    print("="*70)
    
    # Tạo hàm số từ biểu thức symbolic
    x_func = lambdify(t, x_t, 'numpy')
    y_func = lambdify(t, y_t, 'numpy')
    vx_func = lambdify(t, vx_t, 'numpy')
    vy_func = lambdify(t, vy_t, 'numpy')
    L_z_func = lambdify(t, L_z_simplified, 'numpy')
    L_mag_func = lambdify(t, L_magnitude, 'numpy')
    
    # Tạo mảng thời gian
    t_array = np.linspace(t_start, t_end, n_points)
    
    # Tính giá trị
    try:
        x_values = x_func(t_array)
        y_values = y_func(t_array)
        vx_values = vx_func(t_array)
        vy_values = vy_func(t_array)
        L_z_values = L_z_func(t_array)
        L_mag_values = L_mag_func(t_array)
    except Exception as e:
        print(f"Loi khi tinh toan: {e}")
        return
    
    # Loại bỏ các giá trị NaN hoặc inf
    valid_indices = np.isfinite(x_values) & np.isfinite(y_values) & np.isfinite(L_mag_values)
    x_values = x_values[valid_indices]
    y_values = y_values[valid_indices]
    t_array_valid = t_array[valid_indices]
    L_z_values = L_z_values[valid_indices]
    L_mag_values = L_mag_values[valid_indices]
    
    print(f"\nDa tinh toan {len(t_array_valid)} diem hop le")
    
    # Bước 5: Vẽ đồ thị
    fig, axes = plt.subplots(2, 2, figsize=(14, 12))
    
    # Đồ thị 1: Quỹ đạo trong mặt phẳng xy
    ax1 = axes[0, 0]
    ax1.plot(x_values, y_values, 'b-', linewidth=2, label='Quy dao')
    ax1.plot(x_values[0], y_values[0], 'go', markersize=10, label='Diem bat dau')
    ax1.plot(x_values[-1], y_values[-1], 'ro', markersize=10, label='Diem ket thuc')
    ax1.grid(True, alpha=0.3)
    ax1.set_xlabel('x (m)', fontsize=12)
    ax1.set_ylabel('y (m)', fontsize=12)
    ax1.set_title('QUY DAO CHUYEN DONG', fontsize=14, fontweight='bold')
    ax1.legend(fontsize=10)
    ax1.axis('equal')
    
    # Đồ thị 2: x(t) và y(t) theo thời gian
    ax2 = axes[0, 1]
    ax2.plot(t_array_valid, x_values, 'b-', linewidth=2, label='x(t)')
    ax2.plot(t_array_valid, y_values, 'r-', linewidth=2, label='y(t)')
    ax2.grid(True, alpha=0.3)
    ax2.set_xlabel('Thoi gian t (s)', fontsize=12)
    ax2.set_ylabel('Vi tri (m)', fontsize=12)
    ax2.set_title('VI TRI THEO THOI GIAN', fontsize=14, fontweight='bold')
    ax2.legend(fontsize=10)
    
    # Đồ thị 3: Độ lớn mômen động lượng theo thời gian
    ax3 = axes[1, 0]
    ax3.plot(t_array_valid, L_mag_values, 'g-', linewidth=2, label='|L|')
    ax3.grid(True, alpha=0.3)
    ax3.set_xlabel('Thoi gian t (s)', fontsize=12)
    ax3.set_ylabel('Do lon momen dong luong |L| (kg.m^2/s)', fontsize=12)
    ax3.set_title('DO LON MOMEN DONG LUONG THEO THOI GIAN', fontsize=14, fontweight='bold')
    ax3.legend(fontsize=10)
    
    # Đồ thị 4: Thành phần L_z theo thời gian
    ax4 = axes[1, 1]
    ax4.plot(t_array_valid, L_z_values, 'm-', linewidth=2, label='L_z')
    ax4.axhline(y=0, color='k', linestyle='--', alpha=0.3)
    ax4.grid(True, alpha=0.3)
    ax4.set_xlabel('Thoi gian t (s)', fontsize=12)
    ax4.set_ylabel('Thanh phan L_z (kg.m^2/s)', fontsize=12)
    ax4.set_title('THANH PHAN Z CUA MOMEN DONG LUONG', fontsize=14, fontweight='bold')
    ax4.legend(fontsize=10)
    
    plt.tight_layout()
    
    # Lưu đồ thị
    filename = 'momen_dong_luong_ket_qua.png'
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    print(f"\nDa luu do thi vao file: {filename}")
    
    plt.show()
    
    # Hiển thị thống kê
    print("\n" + "="*70)
    print("THONG KE KET QUA")
    print("="*70)
    print(f"Khoi luong m = {m} kg")
    print(f"Khoang thoi gian: [{t_start}, {t_end}] s")
    print(f"\nGia tri momen dong luong:")
    print(f"  |L| trung binh = {np.mean(L_mag_values):.6f} kg.m^2/s")
    print(f"  |L| lon nhat  = {np.max(L_mag_values):.6f} kg.m^2/s")
    print(f"  |L| nho nhat  = {np.min(L_mag_values):.6f} kg.m^2/s")
    print(f"\n  L_z trung binh = {np.mean(L_z_values):.6f} kg.m^2/s")
    print(f"  L_z lon nhat   = {np.max(L_z_values):.6f} kg.m^2/s")
    print(f"  L_z nho nhat   = {np.min(L_z_values):.6f} kg.m^2/s")
    
    print("\n" + "="*70)
    print("HOAN THANH!")
    print("="*70)


def vi_du_1():
    """
    Ví dụ 1: Chuyển động tròn đều
    x(t) = R*cos(ωt)
    y(t) = R*sin(ωt)
    """
    print("\nVI DU 1: CHUYEN DONG TRON DEU")
    print("x(t) = 5*cos(2*t)")
    print("y(t) = 5*sin(2*t)")
    

def vi_du_2():
    """
    Ví dụ 2: Chuyển động ném xiên
    x(t) = v0*cos(α)*t
    y(t) = v0*sin(α)*t - 0.5*g*t^2
    """
    print("\nVI DU 2: CHUYEN DONG NEM XIEN")
    print("x(t) = 10*t")
    print("y(t) = 10*t - 5*t**2")


if __name__ == "__main__":
    print("\n" + "="*70)
    print("CHUONG TRINH TINH TOAN MOMEN DONG LUONG")
    print("="*70)
    print("\nMOT SO VI DU:")
    print("-"*70)
    
    vi_du_1()
    vi_du_2()
    
    print("\n" + "="*70)
    print("\nBat dau nhap lieu...")
    print()
    
    tinh_momen_dong_luong()

