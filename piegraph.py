#!/usr/bin/env python
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt
import numpy as np

def scatter(x, y):
    """
    رسم نمودار پراکندگی (Scatter Plot)
    """
    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, c='b', alpha=0.5)
    plt.title('Scatter Plot')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid(True)
    plt.show()

def line(x, y):
    """
    رسم نمودار خطی (Line Plot)
    """
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, marker='o', linestyle='-', color='r')
    plt.title('Line Plot')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid(True)
    plt.show()

def histogram(data, bins=10):
    """
    رسم نمودار هیستوگرام (Histogram)
    """
    plt.figure(figsize=(8, 6))
    plt.hist(data, bins=bins, color='g', alpha=0.7, edgecolor='black')
    plt.title('Histogram')
    plt.xlabel('Data')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

def distplot(data, bins=10):
    """
    رسم نمودار توزیع (Distribution Plot) با استفاده از matplotlib
    """
    plt.figure(figsize=(8, 6))
    
    # رسم هیستوگرام
    count, bins, ignored = plt.hist(data, bins=bins, color='m', alpha=0.7, edgecolor='black', density=True)
    
    # رسم منحنی تراکم براساس داده های نرمال
    mu, sigma = np.mean(data), np.std(data)
    best_fit_line = (1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-0.5 * ((bins - mu) / sigma) ** 2)
    plt.plot(bins, best_fit_line, '--', color='red')
    
    plt.title('Distribution Plot')
    plt.xlabel('Data')
    plt.ylabel('Density')
    plt.grid(True)
    plt.show()

def heatmap(matrix):
    """
    رسم نمودار هیت‌مپ (Heatmap) با استفاده از matplotlib
    """
    plt.figure(figsize=(8, 6))
    plt.imshow(matrix, cmap='viridis', interpolation='nearest')
    plt.title('Heatmap')
    plt.colorbar()
    plt.show()

def pie(data):
    """
    رسم نمودار دایره‌ای (Pie Chart)
    """
    plt.figure(figsize=(8, 6))
    
    # ساخت لیبل پیش فرض در صورت عدم وجود لیبل
    labels = [f"Section {i+1}" for i in range(len(data))]
    
    plt.pie(data, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title('Pie Chart')
    plt.axis('equal')  # To ensure the pie chart is circular
    plt.show()

    # نمونه‌ای از استفاده از توابع
x = np.linspace(0, 10, 100)
y = np.sin(x)

scatter(x, y)
line(x, y)

data = np.random.normal(0, 1, 1000)
histogram(data)
distplot(data)

matrix = np.random.rand(10, 10)
heatmap(matrix)

pie_data = [10, 20, 30, 40]
pie(pie_data)

    


# In[ ]:




