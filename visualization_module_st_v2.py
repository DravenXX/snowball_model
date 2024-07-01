# 不适用sns库以便部署到云端
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 读取Excel数据
file_path = r'data\snowball_model.xlsx'
# df_500 = pd.read_excel(file_path, sheet_name='df_500')
# df_1000 = pd.read_excel(file_path, sheet_name='df_1000')
point_knock_out_prob_500 = pd.read_excel(file_path, sheet_name='point_knock_out_prob_500')
point_knock_out_prob_1000 = pd.read_excel(file_path, sheet_name='point_knock_out_prob_1000')
pe_knock_out_prob_500 = pd.read_excel(file_path, sheet_name='pe_knock_out_prob_500')
pe_knock_out_prob_1000 = pd.read_excel(file_path, sheet_name='pe_knock_out_prob_1000')
pb_knock_out_prob_500 = pd.read_excel(file_path, sheet_name='pb_knock_out_prob_500')
pb_knock_out_prob_1000 = pd.read_excel(file_path, sheet_name='pb_knock_out_prob_1000')
volatility_knock_out_prob_500 = pd.read_excel(file_path, sheet_name='volatility_knock_out_prob_500')
volatility_knock_out_prob_1000 = pd.read_excel(file_path, sheet_name='volatility_knock_out_prob_1000')
df_500_knock_rate_dict = pd.read_excel(file_path, sheet_name='df_500_knock_rate_dict')
df_1000_knock_rate_dict = pd.read_excel(file_path, sheet_name='df_1000_knock_rate_dict')
df_500_current_loss_ratio_dict = pd.read_excel(file_path, sheet_name='df_500_current_loss_ratio_dict')
df_1000_current_loss_ratio_dict = pd.read_excel(file_path, sheet_name='df_1000_current_loss_ratio_dict')
# 将数据框的列名转换为英文
def rename_columns(df):
    df.columns = ['Metric', 'Total Samples', 'Valid Samples', 'Knockout Probability']
    return df


point_knock_out_prob_500 = rename_columns(point_knock_out_prob_500)
point_knock_out_prob_1000 = rename_columns(point_knock_out_prob_1000)
pe_knock_out_prob_500 = rename_columns(pe_knock_out_prob_500)
pe_knock_out_prob_1000 = rename_columns(pe_knock_out_prob_1000)
pb_knock_out_prob_500 = rename_columns(pb_knock_out_prob_500)
pb_knock_out_prob_1000 = rename_columns(pb_knock_out_prob_1000)
volatility_knock_out_prob_500 = rename_columns(volatility_knock_out_prob_500)
volatility_knock_out_prob_1000 = rename_columns(volatility_knock_out_prob_1000)


# 绘制函数
def plot_data_combined(df, x_col, y_cols, title):
    fig, ax = plt.subplots(figsize=(14, 7))

    x = np.arange(len(df[x_col]))  # x轴位置
    width = 0.4  # 每个柱的宽度

    ax.bar(x - width / 2, df[y_cols[0]], width, label=y_cols[0], color='blue', alpha=0.6)
    ax.bar(x + width / 2, df[y_cols[1]], width, label=y_cols[1], color='red', alpha=0.6)

    ax.set_xticks(x[::len(x) // 10])  # 每隔一定数量显示一个标签
    ax.set_xticklabels(df[x_col][::len(x) // 10])

    ax.set_title(title)
    ax.set_xlabel(x_col)
    ax.set_ylabel('Sample Count')
    ax.legend()

    st.pyplot(fig)


# 绘制函数 - 敲出胜率线性图
def plot_knock_out_prob(df, x_col, y_col, title):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df[x_col], df[y_col], marker='o')
    ax.set_title(title)
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    st.pyplot(fig)


# Streamlit应用
st.title('雪球产品敲出率分析')

# 选择数据框
index_option = st.selectbox(
    'Select Index',
    ('500', '1000'))

# 根据选择映射数据框
if index_option == '500':
    df_map = {
        'Point Knock Out Probability': point_knock_out_prob_500,
        'PE Knock Out Probability': pe_knock_out_prob_500,
        'PB Knock Out Probability': pb_knock_out_prob_500,
        'Volatility Knock Out Probability': volatility_knock_out_prob_500
    }
else:
    df_map = {
        'Point Knock Out Probability': point_knock_out_prob_1000,
        'PE Knock Out Probability': pe_knock_out_prob_1000,
        'PB Knock Out Probability': pb_knock_out_prob_1000,
        'Volatility Knock Out Probability': volatility_knock_out_prob_1000
    }
close_500 = df_500_knock_rate_dict.at[0, 'close']
point_knock_out_prob_500 = df_500_knock_rate_dict.at[0, 'point_knock_out_prob']
pe_500 = df_500_knock_rate_dict.at[0, 'pe']
pe_knock_out_prob_500 = df_500_knock_rate_dict.at[0, 'pe_knock_out_prob']
pb_500 = df_500_knock_rate_dict.at[0, 'pb']
pb_knock_out_prob_500 = df_500_knock_rate_dict.at[0, 'pb_knock_out_prob']
volatility_500 = df_500_knock_rate_dict.at[0, 'volatility']
volatility_knock_out_prob_500 = df_500_knock_rate_dict.at[0, 'volatility_knock_out_prob']

close_1000 = df_1000_knock_rate_dict.at[0, 'close']
point_knock_out_prob_1000 = df_1000_knock_rate_dict.at[0, 'point_knock_out_prob']
pe_1000 = df_1000_knock_rate_dict.at[0, 'pe']
pe_knock_out_prob_1000 = df_1000_knock_rate_dict.at[0, 'pe_knock_out_prob']
pb_1000 = df_1000_knock_rate_dict.at[0, 'pb']
pb_knock_out_prob_1000 = df_1000_knock_rate_dict.at[0, 'pb_knock_out_prob']
volatility_1000 = df_1000_knock_rate_dict.at[0, 'volatility']
volatility_knock_out_prob_1000 = df_1000_knock_rate_dict.at[0, 'volatility_knock_out_prob']

knock_out_prob_description = f"""
### 中证500指数
- 当前点位：**{close_500}**，点位敲出率：**{point_knock_out_prob_500}%**
- P/E: **{pe_500}**，P/E敲出率：**{pe_knock_out_prob_500}%**
- P/B: **{pb_500}**，P/B敲出率：**{pb_knock_out_prob_500}%**
- 波动率: **{volatility_500}%**，波动率敲出率：**{volatility_knock_out_prob_500}%**

### 中证1000指数
- 当前点位：**{close_1000}**，点位敲出率：**{point_knock_out_prob_1000}%**
- P/E: **{pe_1000}**，P/E敲出率：**{pe_knock_out_prob_1000}%**
- P/B: **{pb_1000}**，P/B敲出率：**{pb_knock_out_prob_1000}%**
- 波动率: **{volatility_1000}%**，波动率敲出率：**{volatility_knock_out_prob_1000}%**
"""
st.markdown(knock_out_prob_description)

pe_500_loss = df_500_current_loss_ratio_dict.at[0, "P/E"]
test_pe_500_loss = df_500_current_loss_ratio_dict.at[0, "test P/E"]
volatility_500_loss = df_500_current_loss_ratio_dict.at[0, "Volatility"]
test_volatility_500_loss = df_500_current_loss_ratio_dict.at[0, "test Volatility"]
loss_ratio_500 = df_500_current_loss_ratio_dict.at[0, "Loss Ratio"]

pe_1000_loss = df_1000_current_loss_ratio_dict.at[0, "P/E"]
test_pe_1000_loss = df_1000_current_loss_ratio_dict.at[0, "test P/E"]
volatility_1000_loss = df_1000_current_loss_ratio_dict.at[0, "Volatility"]
test_volatility_1000_loss = df_1000_current_loss_ratio_dict.at[0, "test Volatility"]
loss_ratio_1000 = df_1000_current_loss_ratio_dict.at[0, "Loss Ratio"]

loss_ratio_description = f"""
### 中证500当前点位历史亏损回测
- 回测P/E: **{pe_500_loss}**，实测P/E: **{test_pe_500_loss}**
- 波动率: **{volatility_500_loss}%**，实测波动率: **{test_volatility_500_loss}%**
- 历史回测亏损比例: **{loss_ratio_500}%**

### 中证1000当前点位历史亏损回测
- 回测P/E: **{pe_1000_loss}**，实测P/E: **{test_pe_1000_loss}**
- 波动率: **{volatility_1000_loss}%**，实测波动率: **{test_volatility_1000_loss}%**
- 历史回测亏损比例: **{loss_ratio_1000}%**
"""
st.markdown(loss_ratio_description)

for title, df in df_map.items():

    st.subheader(title)

    # 样本个数和有效样本数柱状图
    st.write(f'{title} - Sample and Knock Out Samples Distribution')
    plot_data_combined(df, x_col=df.columns[0], y_cols=['Total Samples', 'Valid Samples'],
                       title=f'{title} - Sample Count and Valid Samples Distribution')

    # 敲出胜率线性图
    st.write(f'{title} - Knockout Probability Distribution')
    plot_knock_out_prob(df, x_col=df.columns[0], y_col='Knockout Probability',
                        title=f'{title} - Knockout Probability Distribution')

    # 显示数据表
    st.write(df)
