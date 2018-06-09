
Synthetic Dataset Generation -- https://github.com/debidatta/syndata-generation
Usage: python dataset_generator3.py demo_data_dir/objects_dir output_dir --add_distractors
Debug:
- "No module named pb": Install dependencies as described in above github page
- "Module not found pyamg": pip install pyamg or pip3 install pyamg
- "No Module Named Line Dictionary": https://github.com/lospooky/pyblur/issues/5

<To find where ptblur is installed: pip3 show pyblur>
Solution:
This is due to the different syntax for py2 and py3. To fix this issue, 3 places needs to modified.
in pyblur/LinearMotionBlur.py line 8 change to : from .LineDictionary import LineDictionary
in pyblur/Boxblur.py, change all from xxx import xxx =>from .xxx import xxx
incompatibility in lickle load. change pyblur/PsfBlur.py", line 11:
psfDictionary = pickle.load(pklfile) to psfDictionary = pickle.load(pklfile, encoding='latin1')

