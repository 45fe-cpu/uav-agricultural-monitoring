import os,csv
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = Path(os.environ.get("UAV_DATA_DIR", BASE_DIR))
OUTPUT_DIR = Path(os.environ.get("UAV_OUTPUT_DIR", BASE_DIR))
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
import numpy as np
import rasterio
from rasterio.enums import Resampling
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable
from datetime import datetime
files=['10_05-18.tif','10_06-08.tif','10_06-21.tif','10_07-12.tif','10_07-25.tif']
records=[]; images=[]
for fn in files:
 with rasterio.open(str(DATA_DIR / fn)) as s:
  ndvi=s.read(6)
  red=s.read(3); nir=s.read(5)
  valid=np.isfinite(ndvi)&np.isfinite(red)&np.isfinite(nir)&(red+nir>0)&(red<65535)&(nir<65535)&(ndvi>=-1)&(ndvi<=1)
  vals=ndvi[valid]
  date=fn.removeprefix('10_').removesuffix('.tif')
  rec=dict(date='2022-'+date[:2]+'-'+date[3:],file=fn,valid_pixels=int(valid.sum()),valid_percent=round(valid.mean()*100,2),mean_ndvi=round(float(vals.mean()),4),median_ndvi=round(float(np.median(vals)),4),p10=round(float(np.percentile(vals,10)),4),p90=round(float(np.percentile(vals,90)),4),positive_fraction_pct=round(float(np.mean(vals>0)*100),2))
  records.append(rec)
  factor=10
  # Plot decimated aligned pixel grid
  m=ndvi[::factor,::factor].copy(); vv=valid[::factor,::factor]; m[~vv]=np.nan
  images.append(m)
print(records)
with open(OUTPUT_DIR / "ndvi_plot10_summary.csv",'w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=records[0].keys());w.writeheader();w.writerows(records)
fig, axes=plt.subplots(1,5,figsize=(13,10),constrained_layout=True)
for i,(ax,img,r) in enumerate(zip(axes,images,records)):
 ax.imshow(img,cmap='RdYlGn',vmin=-1,vmax=1,interpolation='nearest',aspect='equal')
 ax.set_title(r['date'][5:]+f"\nmedian {r['median_ndvi']:.3f}",fontsize=11)
 ax.axis('off')
fig.suptitle('Wheat plot 10 — NDVI across five UAV surveys (2022)',fontsize=15)
cb=fig.colorbar(ScalarMappable(norm=Normalize(vmin=-1,vmax=1),cmap='RdYlGn'),ax=axes,shrink=.44,location='bottom',pad=.04,aspect=35)
cb.set_label('NDVI (same scale for all dates)')
fig.savefig(OUTPUT_DIR / "wheat_plot10_ndvi_maps.png",dpi=180,bbox_inches='tight'); plt.close(fig)
fig,ax=plt.subplots(figsize=(9,4.5))
dates=[x['date'][5:] for x in records]
ax.plot(dates,[x['median_ndvi'] for x in records],marker='o',label='Median NDVI')
ax.plot(dates,[x['mean_ndvi'] for x in records],marker='s',label='Mean NDVI')
ax.set_ylabel('NDVI');ax.set_xlabel('2022 survey date');ax.grid(alpha=.3);ax.legend()
ax.set_title('Wheat plot 10 — summary NDVI by survey date')
fig.tight_layout();fig.savefig(OUTPUT_DIR / "wheat_plot10_ndvi_trend.png",dpi=180);plt.close(fig)
