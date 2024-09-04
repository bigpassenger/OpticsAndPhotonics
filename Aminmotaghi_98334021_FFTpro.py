#At first we should import diffraction library if you dont have installed this library you have to install it 
#You can do it by pip installaion package ,first go to commands and type {pip install diffractsim}, the machine 
#will download it automatically
import diffractsim
diffractsim.set_backend("CPU") #Change the string to "CUDA" to use GPU acceleration

from diffractsim import MonochromaticField, ApertureFromImage, mm, nm, cm 
#then we need to import MonochromaticField for FFT and ApertureFromImage to import the image and also mm,nm,cm as measurement system



F = MonochromaticField(
    wavelength=483 * nm, extent_x=18 * mm, extent_y=18 * mm, Nx=1024, Ny=1024
)
#extent x & y stands for length and height of the rectangular grid and Nx, Ny the dimension of the grid respectively.

F.add(ApertureFromImage("./Aletter.jpg", image_size=(5.6 * mm, 5.6 * mm), simulation = F))
#F.add(ApertureFromImage("./SingleSlit.jpg", image_size=(5.6 * mm, 5.6 * mm), simulation = F))
#F.add(ApertureFromImage("./Triangle.jpg", image_size=(5.6 * mm, 5.6 * mm), simulation = F))

F.propagate(40*cm) #setting the distance of the plane
rgb = F.get_colors() #for using colors of the wavelenghth (we could use 638nm for having red color and etc here i have used 483nm for blue ابی رنگ عشقه)
F.plot_colors(rgb, xlim=[-7* mm, 7* mm], ylim=[-7* mm, 7* mm])
#IMPORTENT NOTE: THIS PROGRAM ONLY USES JPG IMAGES SO DONT TRY BMP AND PNG...etc FORMATS