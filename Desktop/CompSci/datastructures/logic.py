# logic routines for cs105
# Dave Wonnacott Fall 2006

def precondition(precondition_should_be_true):
	assert(precondition_should_be_true)

def postcondition(postcondition_should_be_true):
	assert(postcondition_should_be_true)

def progress(progress_value):
	assert(progress_value >= 0 and True)  #need more here, obviously


def loop_precondition(loop_precondition_should_be_true):
	assert(loop_precondition_should_be_true)

def loop_postcondition(loop_postcondition_should_be_true):
	assert(loop_postcondition_should_be_true)

def loop_invariant(loop_invariant_should_be_true):
	assert(loop_invariant_should_be_true)

def loop_progress(loop_progress_value):
	assert(loop_progress_value >= 0 and True)  #need more here, obviously
