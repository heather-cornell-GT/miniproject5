class MonsterDiagnosisAgent:
    vitamin_levels = {"+": 1, "0": 0, "-": -1}
    def __init__(self):
        # If you want to do any initial processing, add it here.
        pass

    def solve(self, diseases, patient):
        # Add your code here!
        #
        # The first parameter to this method is a list of diseases, represented as a
        # dictionary. The key in each dictionary entry is the name of a disease. The
        # value for the key item is another dictionary of symptoms of that disease, where
        # the keys are letters representing vitamin names ("A" through "Z") and the values
        # are "+" (for elevated), "-" (for reduced), or "0" (for normal).
        #
        # The second parameter to this method is a particular patient's symptoms, again
        # represented as a dictionary where the keys are letters and the values are
        # "+", "-", or "0".
        #
        # This method should return a list of names of diseases that together explain the
        # observed symptoms. If multiple lists of diseases can explain the symptoms, you
        # should return the smallest list. If multiple smallest lists are possible, you
        # may return any sufficiently explanatory list.
        #
        # The solve method will be called multiple times, each of which will have a new set
        # of diseases and a new patient to diagnose.


        list_of_vitamins = sorted(patient.keys())
        vitamin_length = len(list_of_vitamins)
        patients_vitamin_level = []
        for v in list_of_vitamins:
            value = self.vitamin_levels[patient[v]]
            patients_vitamin_level.append(value)
            print(f'value: {value}')

        if all(t == 0 for t in patients_vitamin_level): ## patient is perfectly healthy qand all vitamins are normal
            return []


        def hmc_depth_first_search(starting_disease, remaining_diseases, running_total_foreach_vitamin, chosen_vitamins):

            return None

        def vitamin_final_sign(x): ##turn any combination of numbers into the vitamin levels defined earlier: -1, 0 , 1
                if x > 0:
                    return 1
                elif x < 0:
                    return -1
                else:
                    return 0

        return []

