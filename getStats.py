#!/usr/bin/env python

#--------------------------------------------------------------------------------------
from launchpadlib.launchpad import Launchpad

print "Connection to launchpad..."
# test case for developing
#a_conn = Launchpad.login_with( 'pythonFlu_getStat', 'staging' )

# for real ppa
a_conn = Launchpad.login_with( 'pythonFlu_getStat', 'production' )

my_launchpad = a_conn.me

total_downloads = 0
Country2DownloadsCount={}
current_version="9.1-SWIG"
ppa_names = ['hhi386', 'hhamd64' ]
for ppa_name in ppa_names:
    print "Connection to ppa \'%s\'"  %ppa_name
    ppa = my_launchpad.getPPAByName( name = ppa_name )
    
    print "Get uploaded binaries..."
    binaries = ppa.getPublishedBinaries()
    for binary in binaries:
        if binary.binary_package_name == 'pythonflu211' and current_version in binary.binary_package_version:
            total_downloads = total_downloads + binary.getDownloadCount()
            for download_instance in binary.getDownloadCounts():
                if not download_instance.country.name in Country2DownloadsCount:
                    Country2DownloadsCount[download_instance.country.name] = download_instance.count
                    pass
                else:
                    Country2DownloadsCount[ download_instance.country.name ] = Country2DownloadsCount[ download_instance.country.name ] + download_instance.count
                    pass
                pass
            pass
        pass

print "Total_downloads  = %s " % total_downloads
for country in Country2DownloadsCount.keys():
    print "\t %s : %s " %( country, Country2DownloadsCount[ country ] )
    pass


#--------------------------------------------------------------------------------------

