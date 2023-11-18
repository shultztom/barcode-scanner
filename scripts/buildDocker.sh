PACKAGE_NAME='barcode-scanner'
PACKAGE_VERSION='1.0.0'
# Build tag with version
docker build -t harbor.shultzlab.com/docker/$PACKAGE_NAME:$PACKAGE_VERSION .
docker push harbor.shultzlab.com/docker/$PACKAGE_NAME:$PACKAGE_VERSION
# Tag with latest
docker tag harbor.shultzlab.com/docker/$PACKAGE_NAME:$PACKAGE_VERSION harbor.shultzlab.com/docker/$PACKAGE_NAME:latest
docker push harbor.shultzlab.com/docker/$PACKAGE_NAME:latest
echo 'Done pushing image'