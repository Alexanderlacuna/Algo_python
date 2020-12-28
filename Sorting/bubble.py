def swap(slices,greater,lesser):
	temp=slices[greater]
	slices[greater]=slices[lesser]
	slices[lesser]=temp
def bubble_sort(slices):
	swapped=True

	while (swapped):
		swapped=False;

		for i in  range(0,len(slices)-1):
			if slices[i]>slices[i+1]:
				swap(slices,i,i+1)
				swapped=True

	return slices
r=bubble_sort([4,3,2,1])
print(r)