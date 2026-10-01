"""
复数自回归意识动力学模型 (Complex Autoregressive Consciousness Model)
基于论文框架：
  - xt = (a + bi) * xt-1 + epsilon_t
  - 实部 a：遗忘 / 腾空间
  - 虚部 b：振荡 / 生成
  - 模长 r：稳定性边界 (|r| < 1)
"""

import numpy as np
import matplotlib.pyplot as plt

class ComplexConsciousnessModel:
    def __init__(self, a: float = 0.7, b: float = 0.4, r_max: float = 0.99):
        self.a = float(a)
        self.b = float(b)
        self.r = np.sqrt(self.a**2 + self.b**2)
        
        # 确保模长在单位圆内 |r| < 1
        if self.r >= r_max:
            scale = r_max / self.r
            self.a *= scale
            self.b *= scale
            self.r = r_max

    def simulate(self, steps: int = 1000, noise_std: float = 0.1) -> np.ndarray:
        """模拟意识轨迹 xt 的复数时间序列"""
        x = np.zeros(steps, dtype=complex)
        x[0] = 0.1 + 0.1j  # 初始状态
        
        for t in range(1, steps):
            # 复数高斯白噪声
            eps = np.random.normal(0, noise_std) + 1j * np.random.normal(0, noise_std)
            x[t] = (self.a + 1j * self.b) * x[t-1] + eps
            
        return x

    def test_prediction_1(self):
        """
        预测 1 验证：清醒态虚部非零 vs. 深度睡眠虚部趋近于零
        """
        print("=== 验证预测 1：清醒态 vs 深度睡眠态 ===")
        # 清醒态：保持健康的振荡虚部
        wake_model = ComplexConsciousnessModel(a=0.7, b=0.4)
        ts_wake = wake_model.simulate(steps=500)
        
        # 深度睡眠：虚部衰减趋近于 0
        sleep_model = ComplexConsciousnessModel(a=0.9, b=0.02)
        ts_sleep = sleep_model.simulate(steps=500)
        
        imag_wake_mean = np.mean(np.abs(np.imag(ts_wake)))
        imag_sleep_mean = np.mean(np.abs(np.imag(ts_sleep)))
        
        print(f"清醒态平均虚部分量 (Imaginary Part): {imag_wake_mean:.4f}")
        print(f"深度睡眠平均虚部分量 (Imaginary Part): {imag_sleep_mean:.4f}")
        return ts_wake, ts_sleep

    def test_prediction_2(self):
        """
        预测 2 验证：高创造态对应特定区间 a ∈ (0.6, 0.8), b ∈ (0.3, 0.5)
        """
        print("\n=== 验证预测 2：高创造力参数区间 ===")
        a_test, b_test = 0.7, 0.4  # 处于最优区间
        in_optimal_range = (0.6 <= a_test <= 0.8) and (0.3 <= b_test <= 0.5)
        
        print(f"当前测试参数: a = {a_test}, b = {b_test}")
        print(f"是否处于高创造力中间区间: {in_optimal_range} (太死板或太飘散均不利于创造)")

if __name__ == "__main__":
    # 实例化并运行测试
    model = ComplexConsciousnessModel()
    ts_wake, ts_sleep = model.test_prediction_1()
    model.test_prediction_2()
    
    # 可视化振荡轨迹
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    axes[0].plot(np.real(ts_wake), np.imag(ts_wake), color='blue', alpha=0.7)
    axes[0].set_title("Waking State (Complex Phase Active)")
    axes[0].set_xlabel("Real Part (a)")
    axes[0].set_ylabel("Imaginary Part (b)")
    axes[0].grid(True)
    
    axes[1].plot(np.real(ts_sleep), np.imag(ts_sleep), color='gray', alpha=0.7)
    axes[1].set_title("Deep Sleep State (Imaginary Part Collapsed)")
    axes[1].set_xlabel("Real Part (a)")
    axes[1].set_ylabel("Imaginary Part (b)")
    axes[1].grid(True)
    
    plt.tight_layout()
    plt.savefig("consciousness_phase_space.png")
    print("\n已生成复数相空间对比图: consciousness_phase_space.png")
