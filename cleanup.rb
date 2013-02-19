EXTS = ['aux', 'fdb_latexmk', 'log', 'pdf']

files = EXTS.map { |t| Dir['**/*\.' + t] }

puts files
