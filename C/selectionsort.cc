const int CUTOFF = 8;

template<typename T>
bool less (T &v, T &w)
{
    return (v < w);
}

template<typename T>
bool eq (T &v, T &w)
{
    return w == v;
}

template <typename T>
void swap (T *a, T *b)
{
    T t = *a;
    *a = *b;
    *b = t;
}

template<typename T>
void insertionSort (vector<T>& input, int lo, int hi) 
{
    for (int i = lo; i <= hi; ++i)
    {
        for (int j = i; j > lo && less(input[j], input[j-1]); --j)
        {
            swap(&input[j], &input[j-1]);
        }
    }
}


template<typename T>
int median3 (vector<T>& input, int indI, int indJ, int indK)
{
    return (less(input[indI], input[indJ]) ?
            (less(input[indJ], input[indK]) ? indJ : less(input[indI], input[indK]) ? indK : indI) :
            (less(input[indK], input[indJ]) ? indJ : less(input[indK], input[indI]) ? indK : indI));
}


template <typename T>
void sort(vector<T>& input, int lo, int hi) 
{ 
    int lenN = hi - lo + 1;

    // cutoff to insertion sort
    if (lenN <= CUTOFF) 
    {
        insertionSort(input, lo, hi);
        return;
    }

    // use median-of-3 as partitioning element
    else if (lenN <= 40) 
    {
        int median = median3(input, lo, lo + lenN / 2, hi);
        swap(&input[median], &input[lo]);
    }

    // use Tukey ninther as partitioning element
    else  
    {
        int eps = lenN / 8;
        int mid = lo + lenN / 2;
        int mFirst = median3(input, lo, lo + eps, lo + eps + eps);
        int mMid = median3(input, mid - eps, mid, mid + eps);
        int mLast = median3(input, hi - eps - eps, hi - eps, hi); 
        int ninther = median3(input, mFirst, mMid, mLast);
        swap(&input[ninther], &input[lo]);
    }

    // Bentley-McIlroy 3-way partitioning
    int iterI = lo, iterJ = hi + 1;
    int iterP = lo, iterQ = hi + 1;

    for (;; ) 
    {
        T v = input[lo];
        while (less(input[++iterI], v))
        {
            if (iterI == hi) 
                break;
        }
        while (less(v, input[--iterJ]))
        {
            if (iterJ == lo)    
                break;
        }
        if (iterI >= iterJ) 
            break;
        swap(&input[iterI], &input[iterJ]);
        if (eq(input[iterI], v)) 
            swap(&input[++iterP], &input[iterI]);
        if (eq(input[iterJ], v)) 
            swap(&input[--iterQ], &input[iterJ]);
    }
    swap(&input[lo], &input[iterJ]);

    iterI = iterJ + 1;
    iterJ = iterJ - 1;
    for (int k = lo + 1; k <= iterP; ++k) 
    {
        swap(&input[k], &input[iterJ--]);
    }
    for (int k = hi  ; k >= iterQ; --k)
    {
        swap(&input[k], &input[iterI++]);
    }

    sort(input, lo, iterJ);
    sort(input, iterI, hi);
}
