import numpy as np, pylab as pl, pyfits as py

def J0837():
    img1 = py.open('/data/ljo31/Lens/J0837/F606W_sci_cutout.fits')[0].data.copy()[30:-30,30:-30] 
    sig1 = py.open('/data/ljo31/Lens/J0837/F606W_noisemap.fits')[0].data.copy()[30:-30,30:-30] 
    psf1 = py.open('/data/ljo31/Lens/J0837/F606W_psf1.fits')[0].data.copy()
    psf1 = psf1/np.sum(psf1)
    img2 = py.open('/data/ljo31/Lens/J0837/F814W_sci_cutout.fits')[0].data.copy()[30:-30,30:-30]
    sig2 = py.open('/data/ljo31/Lens/J0837/F814W_noisemap.fits')[0].data.copy()[30:-30,30:-30] 
    psf2 = py.open('/data/ljo31/Lens/J0837/F814W_psf3.fits')[0].data.copy()
    psf2 = psf2/np.sum(psf2)
    Dx,Dy = -30.,-20.
    OVRS=1
    return img1,sig1,psf1,img2,sig2,psf2,Dx,Dy,OVRS

def J0901():
    img1 = py.open('/data/ljo31/Lens/J0901/F606W_sci_cutout.fits')[0].data.copy()
    sig1 = py.open('/data/ljo31/Lens/J0901/F606W_noisemap.fits')[0].data.copy()
    psf1 = py.open('/data/ljo31/Lens/J0901/F606W_psf2.fits')[0].data.copy()
    psf1 = psf1[5:-6,5:-6]
    psf1 = psf1/np.sum(psf1)
    img2 = py.open('/data/ljo31/Lens/J0901/F814W_sci_cutout.fits')[0].data.copy()
    sig2 = py.open('/data/ljo31/Lens/J0901/F814W_noisemap.fits')[0].data.copy()
    psf2 = py.open('/data/ljo31/Lens/J0901/F814W_psf2.fits')[0].data.copy()
    psf2 = psf2[4:-6,3:-6]
    psf2 = psf2/np.sum(psf2)
    Dx,Dy = 0,0
    OVRS=2
    return img1,sig1,psf1,img2,sig2,psf2,Dx,Dy,OVRS

def J0913(srcno):
    img1 = py.open('/data/ljo31/Lens/J0913/F555W_sci_cutout_big.fits')[0].data.copy()
    sig1 = py.open('/data/ljo31/Lens/J0913/F555W_noisemap_big.fits')[0].data.copy()
    psf1 = py.open('/data/ljo31/Lens/J0913/F555W_psf4.fits')[0].data.copy()
    psf1 = psf1/np.sum(psf1)
    img2 = py.open('/data/ljo31/Lens/J0913/F814W_sci_cutout_big.fits')[0].data.copy()
    sig2 = py.open('/data/ljo31/Lens/J0913/F814W_noisemap_big_edited.fits')[0].data.copy()
    psf2 = py.open('/data/ljo31/Lens/J0913/F814W_psf3.fits')[0].data.copy()
    psf2 = psf2/np.sum(psf2)
    if srcno == 2:
        Dx,Dy = -15.,-20.
    else:
        Dx,Dy = 0,0
    OVRS=1
    return img1,sig1,psf1,img2,sig2,psf2,Dx,Dy,OVRS

def J1125():
    img1 = py.open('/data/ljo31/Lens/J1125/F606W_sci_cutout.fits')[0].data.copy()
    sig1 = py.open('/data/ljo31/Lens/J1125/F606W_noisemap_edited.fits')[0].data.copy()
    psf1 = py.open('/data/ljo31/Lens/J1125/F606W_psf3_filledin.fits')[0].data.copy()
    psf1 = psf1[5:-7,5:-6]
    psf1 = psf1/np.sum(psf1)
    img2 = py.open('/data/ljo31/Lens/J1125/F814W_sci_cutout.fits')[0].data.copy()
    sig2 = py.open('/data/ljo31/Lens/J1125/F814W_noisemap_edited.fits')[0].data.copy()
    psf2 = py.open('/data/ljo31/Lens/J1125/F814W_psf3_filledin.fits')[0].data.copy()
    psf2 = psf2[5:-8,5:-6]
    psf2 = psf2/np.sum(psf2)
    Dx,Dy = 0,0
    OVRS=2
    return img1,sig1,psf1,img2,sig2,psf2,Dx,Dy,OVRS

def J1144():
    img1 = py.open('/data/ljo31/Lens/J1144/F606W_sci_cutout_biggerigger.fits')[0].data.copy()
    sig1 = py.open('/data/ljo31/Lens/J1144/F606W_noisemap_biggerigger.fits')[0].data.copy()
    psf1 = py.open('/data/ljo31/Lens/J1144/F606W_psf1.fits')[0].data.copy()
    psf1 = psf1/np.sum(psf1)
    img2 = py.open('/data/ljo31/Lens/J1144/F814W_sci_cutout_biggerigger.fits')[0].data.copy()
    sig2 = py.open('/data/ljo31/Lens/J1144/F814W_noisemap_biggerigger.fits')[0].data.copy()
    psf2 = py.open('/data/ljo31/Lens/J1144/F814W_psf1.fits')[0].data.copy()
    psf2 = psf2/np.sum(psf2)
    Dx,Dy = -45.,-40.
    OVRS=1
    return img1,sig1,psf1,img2,sig2,psf2,Dx,Dy,OVRS

def J1218():
    img1 = py.open('/data/ljo31/Lens/J1218/F606W_sci_cutout.fits')[0].data.copy()[10:-10,10:-10]
    sig1 = py.open('/data/ljo31/Lens/J1218/F606W_noisemap.fits')[0].data.copy()[10:-10,10:-10]
    psf1 = py.open('/data/ljo31/Lens/J1218/F606W_psf1.fits')[0].data.copy()
    psf1 = psf1/np.sum(psf1)
    img2 = py.open('/data/ljo31/Lens/J1218/F814W_sci_cutout.fits')[0].data.copy()[10:-10,10:-10]
    sig2 = py.open('/data/ljo31/Lens/J1218/F814W_noisemap.fits')[0].data.copy()[10:-10,10:-10]
    psf2 = py.open('/data/ljo31/Lens/J1218/F814W_psf1.fits')[0].data.copy()
    psf2 = psf2/np.sum(psf2)
    Dx,Dy = -50.,-50.
    OVRS=1
    return img1,sig1,psf1,img2,sig2,psf2,Dx,Dy,OVRS

def J1248(maskdust=False):
    print 'need to converge on dustmask choice!'
    img1 = py.open('/data/ljo31/Lens/J1248/F555W_sci_cutout.fits')[0].data.copy()[10:-10,10:-25]
    sig1 = py.open('/data/ljo31/Lens/J1248/F555W_noisemap.fits')[0].data.copy()[10:-10,10:-25]
    psf1 = py.open('/data/ljo31/Lens/J1248/F555W_psf1.fits')[0].data.copy()
    psf1 = psf1/np.sum(psf1)
    img2 = py.open('/data/ljo31/Lens/J1248/F814W_sci_cutout.fits')[0].data.copy()[10:-10,10:-25]
    sig2 = py.open('/data/ljo31/Lens/J1248/F814W_noisemap.fits')[0].data.copy()[10:-10,10:-25]
    psf2 = py.open('/data/ljo31/Lens/J1248/psf2_nopedestal.fits')[0].data.copy()[8:-8,8:-8]
    psf2 = psf2/np.sum(psf2)
    if maskdust:
        sig1 = py.open('/data/ljo31/Lens/J1248/sig1_maskdust7.fits')[0].data.copy()[10:-10,10:-25]
        sig2 = py.open('/data/ljo31/Lens/J1248/sig2_maskdust7.fits')[0].data.copy()[10:-10,10:-25]
    

def J1323(srcno):
    img1 = py.open('/data/ljo31/Lens/J1323/SDSSJ1323+3946_F555W_sci_cutout_big.fits')[0].data.copy()
    sig1 = py.open('/data/ljo31/Lens/J1323/SDSSJ1323+3946_F555W_noisemap_big.fits')[0].data.copy()
    psf1 = py.open('/data/ljo31/Lens/J1323/SDSSJ1323+3946_F555W_psf2.fits')[0].data.copy()
    psf1 = psf1[10:-10,11:-10] 
    psf1 = psf1/np.sum(psf1)
    img2 = py.open('/data/ljo31/Lens/J1323/SDSSJ1323+3946_F814W_sci_cutout_big.fits')[0].data.copy()
    sig2 = py.open('/data/ljo31/Lens/J1323/SDSSJ1323+3946_F814W_noisemap_big.fits')[0].data.copy()
    psf2 = py.open('/data/ljo31/Lens/J1323/SDSSJ1323+3946_F814W_psf3.fits')[0].data.copy()
    if srcno ==2:
        psf2 = psf2[8:-8,9:-8]
    psf2 = psf2/np.sum(psf2)
    Dx,Dy = -20.,-20.
    OVRS=2
    return img1,sig1,psf1,img2,sig2,psf2,Dx,Dy,OVRS

def J1347():
    img1 = py.open('/data/ljo31/Lens/J1347/SDSSJ1347-0101_F606W_sci_cutout.fits')[0].data.copy()
    sig1 = py.open('/data/ljo31/Lens/J1347/SDSSJ1347-0101_F606W_noisemap.fits')[0].data.copy()
    psf1 = py.open('/data/ljo31/Lens/J1347/SDSSJ1347-0101_F606W_psf.fits')[0].data.copy()
    psf1 = psf1[15:-15,15:-15]
    psf1 /= psf1.sum()
    img2 = py.open('/data/ljo31/Lens/J1347/SDSSJ1347-0101_F814W_sci_cutout.fits')[0].data.copy()
    sig2 = py.open('/data/ljo31/Lens/J1347/SDSSJ1347-0101_F814W_noisemap.fits')[0].data.copy()
    psf2 = py.open('/data/ljo31/Lens/J1347/SDSSJ1347-0101_F814W_psf_#2.fits')[0].data.copy()
    psf2 = psf2[15:-15,15:-16]
    psf2 /= psf2.sum()
    Dx,Dy = 0,0
    OVRS=3
    return img1,sig1,psf1,img2,sig2,psf2,Dx,Dy,OVRS

def J1446():
    img1 = py.open('/data/ljo31/Lens/J1446/F606W_sci_cutout.fits')[0].data.copy()
    sig1 = py.open('/data/ljo31/Lens/J1446/F606W_noisemap.fits')[0].data.copy()
    psf1 = py.open('/data/ljo31/Lens/J1446/F606W_psf1.fits')[0].data.copy()
    psf1 = psf1[5:-5,5:-5]
    psf1 = psf1/np.sum(psf1)
    img2 = py.open('/data/ljo31/Lens/J1446/F814W_sci_cutout.fits')[0].data.copy()
    sig2 = py.open('/data/ljo31/Lens/J1446/F814W_noisemap.fits')[0].data.copy()
    psf2 = py.open('/data/ljo31/Lens/J1446/F814W_psf1.fits')[0].data.copy()
    psf2 = psf2[6:-6,7:-7]
    psf2 = psf2/np.sum(psf2)
    Dx,Dy = 0,-20.
    OVRS=1
    return img1,sig1,psf1,img2,sig2,psf2,Dx,Dy,OVRS

def J1605(srcno):
    img1 = py.open('/data/ljo31/Lens/J1605/SDSSJ1605+3811_F555W_sci_cutout2.fits')[0].data.copy()
    sig1 = py.open('/data/ljo31/Lens/J1605/SDSSJ1605+3811_F555W_noisemap2_masked.fits')[0].data.copy() 
    psf1 = py.open('/data/ljo31/Lens/J1605/SDSSJ1605+3811_F555W_psf.fits')[0].data.copy()
    psf1 = psf1[10:-10,10:-10]
    psf1 = psf1/np.sum(psf1)
    img2 = py.open('/data/ljo31/Lens/J1605/SDSSJ1605+3811_F814W_sci_cutout2.fits')[0].data.copy()
    sig2 = py.open('/data/ljo31/Lens/J1605/SDSSJ1605+3811_F814W_noisemap2_masked.fits')[0].data.copy()
    if srcno ==1:
        psf2 = py.open('/data/ljo31/Lens/J1605/F814W_psf_#3.fits')[0].data.copy()  
        psf2= psf2[20:-20,19:-20]
    elif srcno ==2:
        psf2 = py.open('/data/ljo31/Lens/J1605/F814W_psf1new.fits')[0].data.copy()  
    psf2 /= psf2.sum()
    Dx,Dy = -15.,-15.
    OVRS=1
    return img1,sig1,psf1,img2,sig2,psf2,Dx,Dy,OVRS

def J1606():
    img1 = py.open('/data/ljo31/Lens/J1606/F606W_sci_cutout.fits')[0].data.copy()[20:-20,20:-40]
    sig1 = py.open('/data/ljo31/Lens/J1606/F606W_noisemap.fits')[0].data.copy()[20:-20,20:-40]
    psf1 = py.open('/data/ljo31/Lens/J1606/F606W_psf.fits')[0].data.copy()
    psf1 = psf1/np.sum(psf1)
    img2 = py.open('/data/ljo31/Lens/J1606/F814W_sci_cutout.fits')[0].data.copy()[20:-20,20:-40]
    sig2 = py.open('/data/ljo31/Lens/J1606/F814W_noisemap.fits')[0].data.copy()[20:-20,20:-40]
    psf2 = py.open('/data/ljo31/Lens/J1606/F814W_psf.fits')[0].data.copy()
    psf2 = psf2/np.sum(psf2)
    Dx,Dy = -25.,-20.
    OVRS=1
    return img1,sig1,psf1,img2,sig2,psf2,Dx,Dy,OVRS

def J1619():
    img1 = py.open('/data/ljo31/Lens/J1619/F606W_sci_cutout_gross.fits')[0].data.copy()
    sig1 = py.open('/data/ljo31/Lens/J1619/F606W_noisemap_gross.fits')[0].data.copy()
    psf1 = py.open('/data/ljo31/Lens/J1619/F606W_psf1.fits')[0].data.copy()
    psf1 = psf1/np.sum(psf1)
    img2 = py.open('/data/ljo31/Lens/J1619/F814W_sci_cutout_gross.fits')[0].data.copy()
    sig2 = py.open('/data/ljo31/Lens/J1619/F814W_noisemap_gross.fits')[0].data.copy()
    psf2 = py.open('/data/ljo31/Lens/J1619/F814W_psf4big.fits')[0].data.copy()
    psf2 = psf2/np.sum(psf2)
    Dx,Dy = -45.,-50.
    OVRS=2
    return img1,sig1,psf1,img2,sig2,psf2,Dx,Dy,OVRS

def J2228():
    img1 = py.open('/data/ljo31/Lens/J2228/F555W_sci_cutout.fits')[0].data.copy()[120:-110,25:-25]        
    sig1 = py.open('/data/ljo31/Lens/J2228/F606W_noisemap.fits')[0].data.copy()[120:-110,25:-25]    
    psf1 = py.open('/data/ljo31/Lens/J2228/F606W_psf1.fits')[0].data.copy()
    psf1 = psf1/np.sum(psf1)
    img2 = py.open('/data/ljo31/Lens/J2228/F814W_sci_cutout.fits')[0].data.copy()[120:-110,25:-25]   
    sig2 = py.open('/data/ljo31/Lens/J2228/F814W_noisemap.fits')[0].data.copy()[120:-110,25:-25]      
    psf2 = py.open('/data/ljo31/Lens/J2228/F814W_psf1.fits')[0].data.copy()
    psf2 = psf2/np.sum(psf2)
    Dx,Dy = -85.,-60.
    OVRS=1
    return img1,sig1,psf1,img2,sig2,psf2,Dx,Dy,OVRS
