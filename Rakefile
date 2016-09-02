require 'pathname'
DATA_DIR = Pathname 'data'
WRANGLE_DIR = Pathname 'wrangle'
CORRAL_DIR = WRANGLE_DIR.join('corral')
SCRIPTS_DIR = WRANGLE_DIR.join('scripts')
DIRS = {
    :fetched => CORRAL_DIR.join('fetched'),
    :published => DATA_DIR,
}

MIRROR_URL = 'https://github.com/wgetsnaps/ftp.nhtsa.dot.gov--fars/archive/master.zip'


desc 'Setup the directories'
task :setup do
    DIRS.each_value do |p|
        unless p.exist?
            p.mkpath()
            puts "Created directory: #{p}"
        end
    end
end


desc "Download the (2GB+) mirror of the FARS FTP site"
task :fetch_mirror do
  Rake::Task[DIRS[:fetched].join('fars-mirror.zip')].execute()
end


mfile = DIRS[:fetched] / 'fars-mirror.zip'
file mfile do
  sh ['bash', SCRIPTS_DIR / 'fetch_and_unpack_mirror.sh', MIRROR_URL, mfile].join(' ')
end
