import os
import h5py
import pandas as pd

class DalekDataSet():
    @classmethod
    def from_hdf(cls, fname):
        pass

    def __init__(self, parameters, fluxes, wavelength, meta=None):
        self.parameters = parameters
        self.fluxes = fluxes
        self.wavelength = wavelength
        self.meta = meta
        
    def to_hdf(self, fname):
        if os.path.exists(fname):
            raise IOError(f'Path {fname} exists')
        
        with h5py.File(fname, mode='w') as fh:
            fh['fluxes'] = self.fluxes
            fh['wavelength'] = self.wavelength
            
        self.parameters.to_hdf(fname, 'parameters')
        self.meta.to_hdf(fname, 'meta')