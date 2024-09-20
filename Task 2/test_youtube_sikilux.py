# 1.Open the browser Google Chrome
App.open("/usr/bin/google-chrome")
wait(3)

# 2.Click on search bar
click(Location(912, 647))  

# 3.Click to position the cursor in the URL field
click(Location(619, 190))  

# 4.Youtube website search 
type("https://www.youtube.com" + Key.ENTER)
wait(5)  # Adjust according to page load speed

# 5.Check if the YouTube page loaded correctly 
if exists("youtube.png", 10):  
    print("YouTube está cargado correctamente.")
else:
    print("Error: No se pudo cargar YouTube.")
    exit(1)

# 6.Click on video search
if exists("videoCaptura-1.png", 10): 
    click("videoCaptura.png")
    print("Video seleccionado.")
    wait(5) 
else:
    print("Error: No se pudo encontrar el video.")
    exit(1)

# 7.Check if the video started playing
if exists("reproduciendose.png", 10):  
    print("El video está en reproducción.")
else:
    print("Error: El video no está reproduciéndose.")
    exit(1)

# 8.Click on the subscription button
if exists("BotonSuscribirse.png", 10):  
    click("BotonSuscribirse.png",10)
    print("Suscripción realizada.")
else:
    print("Error: No se encontró el botón de suscripción.")
    exit(1)

# 8.Search and Click on the Like Button
if exists("meGusta-1.png", 10):  
    click("meGusta.png")
    print("Me gusta el video.")
else:
    print("Error: No me gusta.")
    exit(1)
   
#9.Scroll down
wheel(WHEEL_DOWN,5)
wait(3)

#10.# Capture an image of the button/add comment

if exists("agregaComentario.png", 10): 
#11. Click on the comment field
    click("agregaComentario.png")
    wait(2)
    
# 12.Write the comment in the field
    type("This comment is automated from SikuliX." + Key.ENTER)
    
#13 If there is a send comment button
    if exists("comentar.png", 5):  
        click("comentar.png")
        print("Comentario añadido correctamente.")
    else:
        print("Comentario escrito, pero no se pudo encontrar el botón de enviar.")
else:
    print("Error: No se pudo cargar la sección de comentarios.")
    exit(1)
 
#End of test
print("Prueba completada exitosamente.")

