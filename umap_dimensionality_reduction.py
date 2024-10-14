# umap_dimensionality_reduction.py
import numpy as np
import pandas as pd
import umap
import matplotlib.pyplot as plt

# 生成隨機數據
data = np.random.rand(100, 5)

# 應用 UMAP 降維
reducer = umap.UMAP()
reduced_data = reducer.fit_transform(data)

# 可視化結果
plt.scatter(reduced_data[:, 0], reduced_data[:, 1])
plt.show()# umap_dimensionality_reduction.py
import numpy as np
import pandas as pd
import umap
import matplotlib.pyplot as plt

# 生成隨機數據
data = np.random.rand(100, 5)

# 應用 UMAP 降維
reducer = umap.UMAP()
reduced_data = reducer.fit_transform(data)

# 可視化結果
plt.scatter(reduced_data[:, 0], reduced_data[:, 1])
plt.show()