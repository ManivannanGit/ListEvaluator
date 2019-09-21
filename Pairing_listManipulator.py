def pairinglist_sum(list,sum):
    
    """
    This function process the list for the given sum value to provide the list of pairs
    """
    
    return [(i,sum-i) for i in list if (sum-i) in list]



# Main Function

def main():
    if __name__ == '__main__':
        sample_list = [0,1,2,3,4,5,6]
        sample_sum = 3
        
        
        print(pairinglist_sum(sample_list,sample_sum))





# Driver Function

main()
