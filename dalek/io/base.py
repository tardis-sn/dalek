import os
import h5py
import pandas as pd
import numpy as np
class DalekDataSet():

    @classmethod
    def from_hdf(cls, fname):
        parameters = pd.read_hdf(fname, 'parameters')
        meta = pd.read_hdf(fname, 'meta')
        with h5py.File(fname, mode='r') as fh:
            spectra = np.array(fh['spectra'])
            wavelength = np.array(fh['wavelength'])

        return cls(parameters, spectra, wavelength, meta)

    def __init__(self, parameters, spectra, wavelength, meta=None):
        self.parameters = parameters
        self.spectra = spectra
        self.wavelength = wavelength
        self.meta = meta
        
    def to_hdf(self, fname, overwrite=False):
        if os.path.exists(fname):
            if overwrite:
                os.remove(fname)
            else:
                raise IOError(f'Path {fname} exists')
        
        with h5py.File(fname, mode='w') as fh:
            fh['spectra'] = self.spectra
            fh['wavelength'] = self.wavelength
            
        self.parameters.to_hdf(fname, 'parameters')
        self.meta.to_hdf(fname, 'meta')
