import collections

class Solution:
    def multiply(self, A, B):
        def encode(sparse_matrix):
            dense_matrix = {}
            for i in range(len(sparse_matrix)):
                for j in range(len(sparse_matrix[0])):
                    if sparse_matrix[i][j]:
                        dense_matrix[(i,j)] = sparse_matrix[i][j]
            return dense_matrix

        def decode(dense_matrix,row,col):
            sparse_matrix = [[0]*col for _ in range(row)]
            for (i,j),val in dense_matrix.items():
                sparse_matrix[i][j] = val

            return sparse_matrix

        A_dense = encode(A)
        B_dense = encode(B)
        print(A_dense)
        print(B_dense)
        ans_dense = collections.defaultdict(int)

        for (i,j) in A_dense.keys():
            for k in range(len(B[0])):
                if (j,k) in B_dense:
                    ans_dense[(i,k)] += A_dense[(i,j)]*B_dense[(j,k)]

        return decode(ans_dense,len(A),len(B[0]))


if __name__ == '__main__':

    mat1 = [[1,0,0],[-1,0,3]]
    mat2 = [[7,0,0],[0,0,0],[0,0,1]]

    ss = Solution()
    res = ss.multiply(mat1, mat2)

    print(res)
