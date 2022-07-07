import os
import h5py
import pandas as pd



class DalekDataSet():
    
    @classmethod
    def from_hdf(cls, fname):
        with pd.HDFStore(fname) as fh:
            parameters = fh['parameters']
            meta = fh['meta']
            wavelength = fh['wavelength']
        
        with h5py.File(fname) as fh:
            spectra = fh['spectra']
        
        return cls(meta, parameters, spectra, wavelength)

    def __init__(self, meta, parameters, spectra, wavelength):
        self.parameters = parameters
        self.spectra = spectra
        self.wavelength = wavelength
        self.meta = meta
        
    def to_hdf(self, fname):
        if os.path.exists(fname):
            raise IOError(f'Path {fname} exists')
        
        with h5py.File(fname, mode='w') as fh:
            fh['spectra'] = self.fluxes
            fh['wavelength'] = self.wavelength
            
        self.parameters.to_hdf(fname, 'parameters')
        self.meta.to_hdf(fname, 'meta')