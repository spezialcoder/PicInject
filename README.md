#    ▄███████▄  ▄█   ▄████████  ▄█  ███▄▄▄▄        ▄█    ▄████████  ▄████████     ███     
  ███    ███ ███  ███    ███ ███  ███▀▀▀██▄     ███   ███    ███ ███    ███ ▀█████████▄ 
  ███    ███ ███▌ ███    █▀  ███▌ ███   ███     ███   ███    █▀  ███    █▀     ▀███▀▀██ 
  ███    ███ ███▌ ███        ███▌ ███   ███     ███  ▄███▄▄▄     ███            ███   ▀ 
▀█████████▀  ███▌ ███        ███▌ ███   ███     ███ ▀▀███▀▀▀     ███            ███     
  ███        ███  ███    █▄  ███  ███   ███     ███   ███    █▄  ███    █▄      ███     
  ███        ███  ███    ███ ███  ███   ███     ███   ███    ███ ███    ███     ███     
 ▄████▀      █▀   ████████▀  █▀    ▀█   █▀  █▄ ▄███   ██████████ ████████▀     ▄████▀   
                                            ▀▀▀▀▀▀   
With picinject you can simply hide files in pictures and extract them again when you need them

### Installing PicInject
First make sure that you have installed python3.
Then type in Console ```python3 setup.py install```


### Using PicInject

Injecting files:```picinject.py --inject --target myImage.jpg --file secret.txt```  
Extracting files from image: ```picinject.py --extract --target myImage.jpg```  
Checking images: ```picinject.py --check --target myImage.jpg```
