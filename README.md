<<<<<<< HEAD
[![ci_validation](https://img.shields.io/github/workflow/status/spacetelescope/jdat_notebooks/ci_validation?label=Notebook%20Validation)](https://github.com/spacetelescope/jdat_notebooks/actions?query=workflow%3Aci_validation)
[![ci_deployment](https://img.shields.io/github/workflow/status/spacetelescope/jdat_notebooks/Build%20and%20deploy%20notebooks?label=HTML%20Deployment&style=flat)](https://github.com/spacetelescope/jdat_notebooks/actions?query=workflow%3ABuild%20and%20deploy%20notebooks)

[![DOI](https://zenodo.org/badge/248772620.svg)](https://zenodo.org/badge/latestdoi/248772620) 

# James Webb Space Telescope Data Analysis Tool Notebooks
=======
# Nancy Grace Roman Space Telescope Notebooks
>>>>>>> 2c25822a (feat: package notebook_data_dependencies as roman_dependencies on PyPI)

The `roman_notebooks` repository contains several workflows and tutorials that demonstrate how to simulate images from, access, and analyze data from the [Nancy Grace Roman Space Telescope](https://roman.gsfc.nasa.gov/)
 (Roman), as well as how to plan observations. Python Jupyter notebooks provide [Tutorials](markdown/tutorials.md)
 on specific topics (e.g., how to run the science data pipeline to calibrate an exposure), while [Science Workflows](markdown/workflows.md) ombine multiple tutorials, along with documentation, to provide a guided, end-to-end experience for a specific science use case.

<<<<<<< HEAD
The ``jdat_notebooks`` repository contains notebooks illustrating workflows for post-pipeline analysis of JWST data. Some of the notebooks also illustrate generic analysis workflows that are applicable to data from other observatories as well. This repository and the notebooks are one component of STScI's larger [Data Analysis Tools Ecosystem](https://jwst-docs.stsci.edu/jwst-post-pipeline-data-analysis).

## Summary and Description

The following [page](https://spacetelescope.github.io/jdat_notebooks/) summarizes the material currently available.

## Installation

To download and execute the notebooks, please read the [detailed instructions](https://spacetelescope.github.io/jdat_notebooks/install.html) . 

## Help

If you uncover any issues or bugs, you can [open an issue on GitHub](https://github.com/spacetelescope/jdat_notebooks/issues/new).  For faster responses, however, we encourage you to submit a JWST Help Desk Ticket: jwsthelp.stsci.edu

## Contributing

Contributions are welcome from both the scientist and developer community.  If you wish to contribute fixes or clarifications to existing notebooks, feel free to do so directly to this repository.  If you wish to contribute new notebooks or major reworks of existing notebooks, see the [contributing instructions](https://github.com/spacetelescope/jdat_notebooks/blob/main/CONTRIBUTING.rst) or the documentation in the [Development section of the instructions](https://spacetelescope.github.io/jdat_notebooks/docs/submitting_notebooks.html).

The notebooks attempt to utilize a number of software packages supported by STScI, including [Astropy](https://www.astropy.org), [glue](http://docs.glueviz.org/en/stable/index.html), [ginga](https://ginga.readthedocs.io/en/latest/), [photutils](https://photutils.readthedocs.io), [specutils](https://specutils.readthedocs.io/en/stable/), [astroimtools](http://astroimtools.readthedocs.io), [imexam](http://imexam.readthedocs.io), [jdaviz](https://jdaviz.readthedocs.io/en/latest/), [asdf](http://asdf.readthedocs.io/en/latest/), [gwcs](https://gwcs.readthedocs.io/en/latest/), and [synphot](http://synphot.readthedocs.io/en/latest/index.html).  Note jdaviz is STScI's JWST Data Analysis Visualization Tool, designed to be used with spectra, IFU cubes, and multi-object spectroscopy (MOS).
=======
The notebooks in this repository are designed for use with the [Roman Research Nexus](https://roman.science.stsci.edu), a cloud-based science platform developed for Roman users. With a [MyST](https://proper.stsci.edu/proper/authentication/auth)
 account, users can access the Nexus and learn how to work with Roman data directly in the cloud. The Nexus is now entering an **Early Access phase**, during which users can explore core functionality while the platform continues to be actively developed and expanded.

## Repository Organization

Notebook tutorials are organized under the `notebooks/` directory. Each notebook is contained within a folder along with a `requirements.txt` file and any other supporting files required to run the notebook.

Markdown documentation files are contained within the `markdown/` folder.

## Local Installation

The notebooks in this repository are designed to work on the Roman Research Nexus for the best user experience. Due to the size of Roman data, local use is not recommended for most users. However, we provide instructions for local installation below. For detailed instructions refer to the [**Working Locally**](markdown/local-run.md) instructions.

## Get Support

Please refer to the [Roman Documentation (RDox)](https://roman-docs.stsci.edu) website for technical documentation about the Roman Space Telescope.

If you need assistance, please submit a ticket through the [Roman Help Desk](https://romanhelp.stsci.edu) portal. Once logged into the help desk, click on "Get Help with the Roman Space Telescope" and then select the "Roman Research Nexus" category and submit your ticket.
>>>>>>> 2c25822a (feat: package notebook_data_dependencies as roman_dependencies on PyPI)
