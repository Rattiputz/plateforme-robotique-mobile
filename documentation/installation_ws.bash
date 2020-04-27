git clone https://github.com/Rattiputz/plateforme-robotique-mobile.git
mkdir -p prm_ws/src
cd prm_ws
catkin_make
cp -r ~/plateforme-robotique-mobile/prm_ws/src ~/prm_ws/
catkin_make
echo "source ~/prm_ws/devel/setup.bash" >> ~/.bashrc
