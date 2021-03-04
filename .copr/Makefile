srpm:
	spectool -g "$(spec)"
	rpmbuild -rr "$(spec)"
	mv *.srpm "$(outdir)"

.PHONY: srpm
