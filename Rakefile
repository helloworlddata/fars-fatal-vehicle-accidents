require 'pathname'
DATA_DIR = Pathname 'data'
WRANGLE_DIR = Pathname 'wrangle'
CORRAL_DIR = WRANGLE_DIR.join('corral')
SCRIPTS_DIR = WRANGLE_DIR.join('scripts')
DIRS = {
    :fetched => CORRAL_DIR.join('fetched'),
    :published => DATA_DIR,
}

desc 'Setup the directories'
task :setup do
    DIRS.each_value do |p|
        p.mkpath()
        puts "Created directory: #{p}"
    end
end
