EXTS = ['aux', 'fdb_latexmk', 'log', 'pdf', 'fls']

files = EXTS.map { |t| Dir['**/*\.' + t] }

puts files
