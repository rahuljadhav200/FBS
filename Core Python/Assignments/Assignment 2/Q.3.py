#. Convert distant given in feet and inches into meter and centimeter.

feet=float(input("Enter the Feet value:"))
inches=float(input("Enter the inches value:"))
total_inches=(feet*12)+inches
meter= total_inches*0.0254
cent= total_inches*2.54
print(f'feet:{feet} and inches:{inches} in meter is:{meter:.2f} and in cent:{cent:.2f}')

