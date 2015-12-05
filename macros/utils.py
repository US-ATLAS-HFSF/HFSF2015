'''
A standard set of utilities that help ease the pain of doing work
'''
import re

dsid_regex = re.compile('\.?(?:00)?(\d{6,8})\.?')
def get_dsid(sample_name):
    '''
    Given a sample name of a standard format, try and extract
    the DSID from it

    sample_name: the filename as a string for a given sample such as "user.mswiatlo:user.mswiatlo.410074.topEW.DAOD_SUSY10.e4143_s2608_s2183_r6869_r6282_p2419_tag_13_xAOD_4_output_xAOD.root"
    return: DSID as a string (example: "410074"
    raise: ValueError if the sample_name doesn't have a valid DSID
    '''
    global dsid_regex
    m = dsid_regex.search(sample_name)
    if m is None: raise ValueError('Can\'t figure out the DSID!')
    return m.group(1)

