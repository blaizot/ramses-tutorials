# REMARK: it is normal the reference value for density is negative. This is the sum of the log of the cell densities.

import osyris 
import numpy as np
import matplotlib.pyplot as plt
import visu as visu_ramses
from scipy.interpolate import griddata
from astropy.io import fits

# Load RAMSES output
data   = osyris.load(4) 
x      = data["xyz"][:,0].values
y      = data["xyz"][:,1].values
z      = data["xyz"][:,2].values
dx     = data["dx"].values
rho    = data["density"].values
vx     = data["velocity"][:,0].values
vy     = data["velocity"][:,1].values
vz     = data["velocity"][:,2].values

#Make maps
xmin = np.amin(x-0.5*dx)
xmax = np.amax(x+0.5*dx)
ymin = np.amin(y-0.5*dx)
ymax = np.amax(y+0.5*dx)
zmin = np.amin(z-0.5*dx)
zmax = np.amax(z+0.5*dx)

nx  = 2**5
dpx = (xmax-xmin)/float(nx)
dpy = (ymax-ymin)/float(nx)
dpz = (zmax-zmin)/float(nx)
xpx = np.linspace(xmin+0.5*dpx,xmax-0.5*dpx,nx)
ypx = np.linspace(ymin+0.5*dpy,ymax-0.5*dpy,nx)
zpx = np.linspace(zmin+0.5*dpz,zmax-0.5*dpz,nx)
grid_x, grid_y, grid_z = np.meshgrid(xpx,ypx,zpx)
points = np.transpose([x,y,z])
z1 = griddata(points,rho,(grid_x,grid_y, grid_z),method='nearest')
z2 = griddata(points,vx ,(grid_x,grid_y, grid_z),method='nearest')
z3 = griddata(points,vy ,(grid_x,grid_y, grid_z),method='nearest')
z4 = griddata(points,vz ,(grid_x,grid_y, grid_z),method='nearest')

rho_proj2 = np.sum(z1, axis=0) #proj along y-axis
rho_proj2_file = "rho_proj_along_yaxis.fits"
rho_proj1 = np.sum(z1, axis=1) #proj along x-axis
rho_proj1_file = "rho_proj_along_xaxis.fits"
rho_proj3 = np.sum(z1, axis=2) #proj along z-axis
rho_proj3_file = "rho_proj_along_zaxis.fits"
vx_proj = np.sum(z2, axis=1)
vx_proj_file = "vx_proj.fits"
vy_proj = np.sum(z3, axis=0)
vy_proj_file = "vy_proj.fits"
vz_proj = np.sum(z4, axis=2)
vz_proj_file = "vz_proj.fits"

#Save maps in .fits format
f = fits.PrimaryHDU(rho_proj2)
hdu = fits.HDUList([f])
hdu.writeto(rho_proj2_file,  overwrite = True)

f = fits.PrimaryHDU(rho_proj1)
hdu = fits.HDUList([f])
hdu.writeto(rho_proj1_file,  overwrite = True)

f = fits.PrimaryHDU(rho_proj3)
hdu = fits.HDUList([f])
hdu.writeto(rho_proj3_file,  overwrite = True)

f = fits.PrimaryHDU(vx_proj)
hdu = fits.HDUList([f])
hdu.writeto(vx_proj_file,  overwrite = True)

f = fits.PrimaryHDU(vy_proj)
hdu = fits.HDUList([f])
hdu.writeto(vy_proj_file,  overwrite = True)

f = fits.PrimaryHDU(vz_proj)
hdu = fits.HDUList([f])
hdu.writeto(vz_proj_file,  overwrite = True)
