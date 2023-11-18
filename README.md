# barcode-scanner

An API made with fastapi, numpy, cv2, and pyzbar to read image uploads and return barcode information

#### Local Dev - Mac

1. zbar - on Mac

`brew install zbar`

`mkdir ~/lib`

`ln -s $(brew --prefix zbar)/lib/libzbar.dylib ~/lib/libzbar.dylib`

#### Docker

1. `./scripts/buildDocker.sh`
2. `./scripts/runDockerImage.sh`