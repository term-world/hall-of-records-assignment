
| Date              |          |
|:------------------|:---------|
| 16 October 2022 | Assigned |
| 23 October 2022 | Due      |
| Status            | [![GatorGrader](../../actions/workflows/main.yml/badge.svg)](../../actions/workflows/main.yml) |

# DATA DONE, MAYOR DECREES DECISIVE DEED: CITIZENS TO COMPUTE REPRESENTATIVE RESIDENT CRITERIA

**Reported by `Official Mayor-Endorsed News` on `16 October 2022`**

Maintaining a healthy community is _everyone's job_ and so is neighborhood surveillance! As the Mayor 
described to O.M.E.N. (Offical Mayor Endorsed News), "I, your Mayor, look to you, the great citizens
of `term-world` to help define the ideal citizen contributors. To you, people of this fair city, I (your Mayor) ask for the profile of the most resilient, representative residents!"

As O.M.E.N. has learned, this means trawling through much of the data kept at the newly-restored city `datamart` to uncover the statistics describing the very demonstrative denizens which detail the ideal community member. This data digs deep. Using words that O.M.E.N. was told to say, it covers all of the behaviors that a mindful member of `term-world` must aspire to. "We've been collecting data on you, our citizens, this whole time!" the Mayor reiterated.

Will you, great residents of `term-world` help define the future of this digital world? The Mayor certainly hopes so, saying "[y]our Mayor--of course, that's me--depends on you to compile every last criterion toward identifying the luminaries of our land!" To those who meet the basic benchmarks go all the spoils! Just exactly what those spoils are, the Mayor's Office declines to say.

## Overview

In this set of activities we cover:

* `dictionary` data structures
* a review of `list`s and `iteration` (`for`/`while` loops)
* revisiting `functions`
* exploring more basic data science

You'll complete one main task, supported by three sub-tasks:

* An average of all columns of the data (main task), using
  * a `function` that returns rows matching a minimum value in a given column (sub-task)
  * a `function` that totals the numeric values of a given column (sub-task)
  * a report of the average of a given column (sub-task)

As with `datamart`, there are plenty of opportunities for improvements to how you find various statistics about the data. Keep an open mind and a keen eye to the particularly annoying inconveniences of the `Processor` program.

### Supporting media

[![YouTube thumbnail](http://img.youtube.com/vi/SgvHztqxq3s/hqdefault.jpg)](https://youtube.com/playlist?list=PLJvBsjwXNdlGQVIsvaHgamBszfCO6750Z)

## Accessing `hall-of-recods` Content

In order to complete the workload for the `hall-of-records` you'll first need to `clone` the `hall-of-records` repository into your `workshop`.

When you `clone` a repository you're duplicating its contents and adding them to your local workspace. Since you'll be working collaboratively with your neighbors, you'll each need your own copy of the `hall-of-records` to work with.

In order to keep some of the magic (read: somewhat convoluted code) that makes `term-world` work the way it does, **you are required to clone all additional repositories within the `workshop`, located within your `garage`.**

Head to GitHub and:
* click on the green `Code` button
* ensure that `SSH` is selected
* copy the link that appears in the window below

It might look something like `git@github.com:term-world/hall-of-records-dluman`.

Once you've copied this link, navigate to your terminal window and ensure you're still in the appropriate place (in this case, the topmost level of your `workshop`). Then, enter the command:

```
git clone COPIED-LINK-HERE
```

Be sure to replace the fragment `COPIED-LINK-HERE` with the link you copied. In the example regarding `hall-of-records-dluman`, the full command would look like:

```
git clone git@github.com:term-world/hall-of-records-dluman
```

While `pull` is used to *update* the contents of a repository that already exists in your local workspace, `clone` is used to *replicate* the contents of a repository from GitHub and copy them to your local workspace.

## Completing `hall-of-records` content

The `hall-of-records` has just one file: `Processor.py`. Functionality of the `Processor` has largely been completed for you. The work left up to you is to write the `function`s required to produce the statistical report requested in the `reflection.md`.

This program uses one `global` variable to house the data in the table and the names of columns. Use:

|Variable |Purpose |
|:--------|:-------|
|DATA†     |Holds columns and data from table |

`†` This is a departure from the last assignment; see what conveniences `dictionary`s provide you!

### `Processor.py`

Leverges the `main` function to:

* Work out options for the `Processor`'s main menu
* Provides _at least_ two `function`s outlined in the `task`/`subtask` breakdown above


|Function name |Parameters  |Return type | Description                                               |
|:-------------|:-----------|:-----------|:----------------------------------------------------------|
|search_rows        |Field to search (`str`), term/number to search (`any`)       |`list`      |Returns _all_ rows which are greater than or equal to a given search criteria |
|total_column       |Field to total (`str`)             |`int`       |Returns the total of all numeric data in a given column |

Your [reflection](office/reflection.md) should report the outcomes of these operations.

### Writing

Choose one of the following.

#### Reflection

All of the above tasks completed, finish the reflection located in the `office` folder.

#### Protesting

You may protest completing this assignment by writing an `editorial.md` in the `office` _instead_ of a `reflection.md`. Doing so _does not mean_ not completing the code for this assignment. Rather, it indicates that you should compose an evidence-based argument that uses your analysis to persuade your fellow citizens to your cause.

## Evaluating `hall-of-records` Content

In order to run the `grader` for this week's work, you'll need to be in the topmost level of the `hall-of-records` folder (which should have been cloned within the `workshop`). Once there, run the command:

```
gatorgrade
```

### Making an improvement proposal

This assignment begins your opportunity to propose and improve the world of `term-world` at-large. For this assignment, proposals may include making graphics to improve the `bodega` site experience, creating new items or actions in the `traffic-circle` itself or another assignment-related improvement not contemplated in the prior narrow categories.

To make an improvement proposal, you must _create an issue_ on this repository. Do so by:

* clicking the `Issues` tab at the top of the page.
* clicking the green `New Issue` button
* selecting the `Improvement Proposal` template 

**You must fill out the entire template and wait for Mayoral approval before starting the improvement.**

## Submitting `hall-of-records` Content

When you're ready to push to GitHub, do the normal `add` and `commit` routines. Recall:

```
git add NAME_OF_FILE_OR_DIRECTORY_TO_ADD
```

You may need to do this for either:

* Individual files (i.e. `git add table_builder.py`)
* Directories (i.e. `git add analyzer`)

```
git commit -m "Descriptive commit message"
```

Of course, don't forget the last step: to `git push`
