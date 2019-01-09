import multiprocessing as mp

def main():
    print("cpus =", mp.cpu_count())

if __name__ == "__main__":
    main()
