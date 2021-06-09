# SFreeze
A small package for storing serialized python objects persitantly using Amazon AWS S3

## Usage
**SECURITY WARNING!!!**

This library uses the python Pickle module to perform serialization.
Be careful when thawing objects as it can lead to arbitrary code exectuion. 

**Only use this library on objects you trust**

To use sfreeze you must have aws cli credentials setup that have access to read and write to the target S3 bucket.

### Freezing an object
```python
from sfreeze import s3_freeze

variable_to_freeze = 'some variable'

# s3_freeze takes the object, bucket, and optional key
# you can also send it other keyword args and they will 
# get passed to a boto3.client('s3').put_object call
object_id = s3_freeze(variable_to_freeze, 'bucket', 'optional_key')
```

### Thawing an object
```
from sfreeze import s3_thaw

# s3_thaw takes the object_id returned from s3_freeze,
# you can also send it other keyword args and they will 
# get passed to a boto3.client('s3').put_object call
thawed_variable = s3_thaw(object_id)
```