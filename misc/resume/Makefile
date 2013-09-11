proj=resume
SRC = resume.tex
OUT = $(SRC:.tex=.pdf)

all: $(OUT)

%.pdf: %.tex functions.tex
	xelatex $<
	xelatex $<

clean:
	-rm *.pdf
	-rm *.aux
	-rm *.log
	-rm *.out
	-rm *~
