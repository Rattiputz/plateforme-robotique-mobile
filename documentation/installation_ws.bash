git clone https://github.com/Rattiputz/plateforme-robotique-mobile.git ~/plateforme-robotique-mobile
mkdir -p ~/prm_ws/src
cp -r ~/plateforme-robotique-mobile/prm_ws/src ~/prm_ws/
cd ~/prm_ws
catkin_make -DCMAKE_BUILD_TYPE=Release
echo "source ~/prm_ws/devel/setup.bash" >> ~/.bashrc
