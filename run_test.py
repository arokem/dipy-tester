import nose
import dipy.data as dpd
funcs = [k for k in dpd.__dict__.keys() if k.startswith('fetch')]

for k in funcs:
    dpd.__dict__[funcs[0]]()

config = nose.config.Config(verbosity=2)
nose.runmodule('dipy', config=config)
