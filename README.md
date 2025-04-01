use N randomly moving and colliding scatters form various images. Dynamic effects are achieved by calculating the particle positions and rendering them to the plot in real time.

# file describe
root
├── rsc                     # patterns, in the csv file, all the 1s form a pattern.
│   ├── 50100.csv
│   ├── 50100C.csv
│   └── 50100L.csv
├── excel_word.py           # get pattern in csv and reform to one-dimension index. 
├── figshow.py              # render the scatter position in real time by plot.
├── main.py                 # init and mainloop.
├── scatter_item.py         # calculation functions for scatter speed, position, collision, etc.
└── shape_read.py

# RUN
python -u main.py

# NOTE
recommend python 3.6.13, some plot libraries in higher versions of Python operate too slowly for unknown reasons.

# TODO
- read shape from image.
- read shape from hand write.
