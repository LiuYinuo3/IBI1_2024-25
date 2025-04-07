import matplotlib.pyplot as plt
uk_countries = [57.11, 3.13, 1.91, 5.45]
zjnb_provinces = [65.77, 41.88, 45.28, 61.27, 85.15]
uk_data = {"England": 57.11,"Wales": 3.13,"Northern Ireland": 1.91,"Scotland": 5.45}
china_data = {"Zhejiang": 65.77,"Fujian": 41.88,"Jiangxi": 45.28,"Anhui": 61.27,"Jiangsu": 85.15}

# Create and print sorted lists
uk_sorted = sorted(uk_data.items(), key=lambda x: x[1], reverse=True)
china_sorted = sorted(china_data.items(), key=lambda x: x[1], reverse=True)

#print the sorted values
print("Sorted UK countries (name: population in millions):")
for country, pop in uk_sorted:
    print(f"{country}: {pop}")
print("\nSorted Zhejiang-neighboring provinces (name: population in millions):")
for province, pop in china_sorted:
    print(f"{province}: {pop}")

# Create pie charts
plt.figure(figsize=(16, 8))

# UK Pie Chart
plt.subplot(1, 2, 1, aspect='equal') #stay in the left
wedges_uk, texts_uk, autotexts_uk = plt.pie(
    uk_countries,labels=uk_data.keys(),
    autopct=lambda p: f'{p:.1f}%\n({p*sum(uk_countries)/100:.2f}M)', #show population and proportion of each part
    colors= ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A'],
    wedgeprops={'linewidth': 1, 'edgecolor': 'white'},
    textprops={'fontsize': 9}
)
plt.setp(autotexts_uk, size=8, weight="bold")
plt.title('UK Population Distribution (2022)\n', fontsize=12, fontweight='bold')

# China Pie Chart
plt.subplot(1, 2, 2, aspect='equal') #stay in consistent with the chart of UK population
wedges_china, texts_china, autotexts_china = plt.pie(
    zjnb_provinces,
    labels=china_data.keys(),
    autopct=lambda p: f'{p:.1f}%\n({p*sum(zjnb_provinces)/100:.2f}M)',
    colors=['#FFD166', '#06D6A0', '#118AB2', '#EF476F', '#073B4C'],
    wedgeprops={'linewidth': 1, 'edgecolor': 'white'},
    textprops={'fontsize': 9}
)
plt.setp(autotexts_china, size=8, weight="bold")
plt.title('Zhejiang-Neighboring Provinces Population (2022)\n', fontsize=12, fontweight='bold')

# Add title and adjust layout
plt.suptitle('Population Distribution Comparison', fontsize=16, fontweight='bold', y=1.05)
plt.tight_layout()

# Save and show
plt.savefig('population_distribution.png')
plt.show()