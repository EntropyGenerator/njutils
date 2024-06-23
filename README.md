# NJUtils
Some utilities for NJUer
```python
pip install -r requirements.txt
```
### Dormitory electricity tracer
It can polling remaining electricity of the dormitory, and plot the results.  
To use it, you have to create an .env file and fill in the parameters.
```
NJU_USERNAME=xxxxxxxxxx
NJU_PASSWORD="xxxxxxxx"

# After filling params above, you can run dormitory_electicity.py first to get values to fill params below.
CAMPUS_ID=xx
AREA_ID=x
BUILDING_ID="xxxxxxxxxxxxxx_xxxxxxxxxxxxxx"
ROOM_ID=xxxxxxxxxxxx
```
After filling these, you can run `dormitory_electricity_tracer.py` using a bash loop, such as
```bash
while true
do
    python dormitory_electricity_tracer.py
    sleep 10m
done
```
You will get a `result.png` after running for sometime.
#### Reference
Login code from [NJUlogin](https://github.com/do1e/NJUlogin).